from flask import Flask, request, jsonify, render_template

import requests
import pandas as pd

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os

from langdetect import detect
from deep_translator import GoogleTranslator
import re

from joblib import load

app = Flask(__name__)

# 저장된 모델 로드
model_filename = 'decision_tree_model.joblib'
model = load(model_filename) 

chrome_options = webdriver.ChromeOptions()

# heroku 서버용
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Google 번역기 객체 생성
translator = GoogleTranslator(source='auto', target='ko')
  
def get_destination_location(destination):
    print(f'get_destination_location for {destination}')

    API_KEY = "AIzaSyBOk6m0_w3Rzmj0x3bmzNbisuE2uNYFq-Q"

    # Google Maps Geocoding API로 여행지 위치 데이터 가져오기
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={destination}&key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    location = data['results'][0]['geometry']['location']
    latitude = location['lat']
    longitude = location['lng']
    destination_location = (latitude, longitude)

    return destination_location

def get_info_from_tripadvisor(destination):
    print(f'get_info_from_tripadvisor for {destination}')  

    url = f'https://www.tripadvisor.co.kr/Search?q={destination}&ssrc=g'
    driver.get(url)
    driver.implicitly_wait(10)

    results = driver.find_elements(By.CLASS_NAME,'prw_search_search_result_geo')
    
    place_info_list = []
    # 각 결과에서 여행지의 타이틀, 이미지 URL, 설명 가져오기
    for result in results[1:4]:
        title = result.find_element(By.CLASS_NAME, 'result-title').text
        style_value = result.find_element(By.CLASS_NAME,'inner').get_attribute('style')
        image_url = style_value.split('(')[1].split(')')[0]
        try:
            description = result.find_element(By.CLASS_NAME, 'geo-description').text
        except NoSuchElementException:
            description = '설명 없음.'
        onclick_value = result.find_element(By.CLASS_NAME, "ui_columns").get_attribute("onclick")
        url_match = re.search(r"'/([^']+)'", onclick_value)
        link = 'https://www.tripadvisor.co.kr/' + url_match.group(1)

        if detect(description) == 'en':
            try:
                translated_description = translator.translate(text=description)
                translated_description = '. '.join(translated_description.split('.')).strip()
            except Exception as e:
                print(f"번역 오류: {e}")
                translated_description = description
        else:
            translated_description = description
            
        if not translated_description.endswith('.'):
            translated_description += '...'

        place_info = {
            'title': title,
            'image_url': image_url,
            'description': translated_description,
            'link': link
        }
        place_info_list.append(place_info)

    print(f'place_info_list len: {len(place_info_list)}')
    return place_info_list

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 입력 받기
        data = request.get_json(force=True)
        age = float(data['age'])
        sex = float(data['sex'])
        area = float(data['area'])
        income = float(data['income'])

        area_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if (area < 15):
          area_list[int(area)] = 1
    
        #입력된 사용자 정보 인코딩
        encoded_user_info = [age, income, sex, *area_list]
        # 입력 데이터로 예측
        predicted_value = model.predict([encoded_user_info])

        #print(encoded_user_info)
        predicted_cluster = predicted_value[0]
        print(f"사용자의 군집 예측: {predicted_cluster}")
        
        # 해당 군집의 관심도 상위 3개 지역
        top_columns_df = pd.read_csv('top_columns.csv', index_col=0)
        top_destinations = top_columns_df.loc[predicted_cluster].str.replace('여행관심값', '')
        print(top_destinations)
        
        result_list = []
        for destination in top_destinations:
            # 상위 3개 지역의 위도, 경도 정보 가져오기
            destination_location = get_destination_location(destination)
            print(destination_location)
            # 해당 지역의 여행지 3개 정보 가져오기
            place_info_list = get_info_from_tripadvisor(destination)

            popup_content = ''
            for place_info in place_info_list:
                title_with_link = f'<a href="{place_info["link"]}" target="_blank" style="font-size: 20px;">{place_info["title"]}</a>'
                popup_content += f'<h3 class="title is-4">{title_with_link}</h3><div class="has-text-centered"><img src={place_info["image_url"]} width="450" style="display: block; margin: 0 auto;"/></div><br><p class="subtitle is-6">{place_info["description"]}</p><br><br>'
            
            result_list.append([destination_location, popup_content, destination])
            print(f'{destination} 여행지 (위도, 경도): {destination_location}')
                    
        # 예측 결과 반환
        return jsonify(result_list)
    
    except Exception as e:
        return jsonify({'error': str(e)})
  

if __name__ == '__main__':
    app.run(port=5000)