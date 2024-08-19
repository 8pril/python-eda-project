# python-eda-project
사용자 정보에 기반한 여행지 추천

# 1. 프로젝트 소개

### 주제

- 성별, 연령대, 거주지, 소득수준등 사용자 특성에 따라 관심 가질 확률이 높은 여행 지역을 알려 주고 각 지역의 여행 장소를 추천하는 서비스를 구축한다.

# **2. 사용 데이터**

### **데이터 소개**

[문화빅데이터 플랫폼](https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=2bc30b30-4129-11ec-a107-3b8bd6a15b10)

- 온라인(PC모바일) 소비자 서베이 데이터(2015.8월부터 매주 수집)
- 해외 12개지역에 대한 관심도(요즘 ‘OOO’을 가보고 싶다는 생각이 예전에 비해 … )를 5점 척도로 응답.
- 12개 지역 : 중국, 일본, 홍콩마카오, 동남아시아, 중동서남아시아, 미국캐나다, 남미중남미, 서유럽북유럽, 동유럽, 남유럽, 남태평양, 아프리카
- 본 데이터 셋에는 응답자 특성(성별, 연령대, 거주지역, 소득수준 등)이 포함됨.

### **데이터 활용**

- 해외여행의 지역 선호도로 단기 시장 예측

### **데이터 출처**

- ㈜컨슈머인사이트 정기 기획조사 **‘주례(weekly) 여행 행태 및 계획조사' (연간 26,000명)**

### **컬럼 정의서**

| 순서 | 컬럼영문명 | 컬럼한글명 | 데이터타입 | 길이 | PK여부 | NOT NULL여부 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | RESPOND_ID | 응답자ID | VARCHAR | 50 | Y | Y |
| 2 | EXAMIN_BEGIN_DE | 조사시작일자 | VARCHAR | 8 | Y | Y |
| 3 | SEXDSTN_FLAG_CD | 성별구분코드 | VARCHAR | 30 | N | Y |
| 4 | AGRDE_FLAG_NM | 연령대구분명 | VARCHAR | 200 | N | Y |
| 5 | ANSWRR_OC_AREA_NM | 답변자거주지역명 | VARCHAR | 200 | N | Y |
| 6 | HSHLD_INCOME_DGREE_NM | 가구소득정도명 | VARCHAR | 200 | N | Y |
| 7 | CHINA_TOUR_INTRST_VALUE | 중국여행관심값 | VARCHAR | 200 | N | Y |
| 8 | JP_TOUR_INTRST_VALUE | 일본여행관심값 | VARCHAR | 200 | N | Y |
| 9 | HONGKONG_MACAU_TOUR_INTRST_VALUE | 홍콩마카오여행관심값 | VARCHAR | 200 | N | Y |
| 10 | SEASIA_TOUR_INTRST_VALUE | 동남아시아여행관심값 | VARCHAR | 200 | N | Y |
| 11 | MDLEST_SWASIA_TOUR_INTRST_VALUE | 중동서남아시아여행관심값 | VARCHAR | 200 | N | Y |
| 12 | USA_CANADA_TOUR_INTRST_VALUE | 미국캐나다여행관심값 | VARCHAR | 200 | N | Y |
| 13 | SAMRC_LAMRC_TOUR_INTRST_VALUE | 남미중남미여행관심값 | VARCHAR | 200 | N | Y |
| 14 | WEURP_NEURP_TOUR_INTRST_VALUE | 서유럽북유럽여행관심값 | VARCHAR | 200 | N | Y |
| 15 | EEURP_TOUR_INTRST_VALUE | 동유럽여행관심값 | VARCHAR | 200 | N | Y |
| 16 | SEURP_TOUR_INTRST_VALUE | 남유럽여행관심값 | VARCHAR | 200 | N | Y |
| 17 | SPCPC_TOUR_INTRST_VALUE | 남태평양여행관심값 | VARCHAR | 200 | N | Y |
| 18 | AFRICA_TOUR_INTRST_VALUE | 아프리카여행관심값 | VARCHAR | 200 | N | Y |

### **데이터 수집 방법**

20230821~20230925까지의 원본 데이터를 병합하여 약 1500개의 16개의 범주형 변수 데이터를 가진 데이터셋을 생성하여 분석 진행.

결측치는 ‘가구소득정도명’ 변수에서만 발견되었으며 EDA 분석을 통해 적합한 방법으로 처리.

# **3. 데이터 분석**

### **기초통계량**

| 연령대구분명 | 가구소득정도명 | 중국여행관심값 | 일본여행관심값 | 홍콩마카오여행관심값 | 동남아시아여행관심값 | 중동서남아시아여행관심값 | 미국캐나다여행관심값 | 남미중남미여행관심값 | 서유럽북유럽여행관심값 | 동유럽여행관심값 | 남유럽여행관심값 | 남태평양여행관심값 | 아프리카여행관심값 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| count | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 | 1495.000000 |
| mean | 41.438127 | 2.749833 | 2.077592 | 2.943813 | 2.858194 | 3.184615 | 2.377258 | 3.272241 | 2.671572 | 3.393311 | 3.206020 | 3.268896 | 3.399331 |
| std | 13.826425 | 1.017398 | 0.998325 | 1.264615 | 0.999309 | 1.059491 | 1.054482 | 1.012703 | 1.035431 | 1.046679 | 1.068142 | 1.048331 | 1.002206 |
| min | 20.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 | 1.000000 |
| 25% | 30.000000 | 2.000000 | 1.000000 | 2.000000 | 2.000000 | 3.000000 | 1.000000 | 3.000000 | 2.000000 | 3.000000 | 3.000000 | 3.000000 | 3.000000 |
| 50% | 40.000000 | 3.000000 | 2.000000 | 3.000000 | 3.000000 | 3.000000 | 2.000000 | 3.000000 | 3.000000 | 3.000000 | 3.000000 | 3.000000 | 3.000000 |
| 75% | 50.000000 | 4.000000 | 3.000000 | 4.000000 | 3.000000 | 4.000000 | 3.000000 | 4.000000 | 3.000000 | 4.000000 | 4.000000 | 4.000000 | 4.000000 |
| max | 60.000000 | 4.000000 | 5.000000 | 5.000000 | 5.000000 | 5.000000 | 5.000000 | 5.000000 | 5.000000 | 5.000000 | 5.000000 | 5.000000 | 5.000000 |

가구소득명과 여행관심값들은 데이터의 값이 string이었기 때문에 레이블 인코딩을 통해 integer로 바꿔주었음.

### **결측치 처리**

| \가구소득정도명
연령대구분명 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 20 | 55 | 76 | 40 | 76 |
| 30 | 34 | 115 | 69 | 56 |
| 40 | 24 | 75 | 120 | 93 |
| 50 | 29 | 73 | 106 | 133 |
| 60 | 51 | 89 | 99 | 82 |

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/428625a4-9ad9-475f-928a-cd28653d0d3a/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/82c3edfc-9d62-4f7d-a9b2-34311837a24d/Untitled.png)

연령대가 높을수록 가구 소득 정도가 높다는 것을 확인하여 연령대와 가구 소득 사이에 어느 정도의 연관관계가 있다고 판단. 또한 카이제곱 검정을 시행하여 p-value가 1.768e-16으로 0.05보다 작아 두 변수 사이에 독립성이 없다는 귀무가설을 기각할 수 있었음. 두 변수 사이에 유의미한 관계가 있다고 판단. 따라서 범주형 변수인 가구소득정도의 결측치를 처리하기 위해 해당 연령대의 최빈값으로 값을 채워 이후 분석 진행.

### **응답자 특성 변수 4개 피처별 분석**

- 성별에 따른 지역별 관심도
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/ee2e26a2-891a-42a9-9f74-18dbf3aad3ad/Untitled.png)
    
- 연령대에 따른 지역별 관심도
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/dd32b358-6e1e-4195-913e-831d018ee8dd/Untitled.png)
    
- 거주지에 따른 지역별 관심도
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/90fd35fd-42bb-4f1a-a0d7-bc401e9f9565/Untitled.png)
    
- 소득수준에 따른 지역별 관심도
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/257efd6e-44ae-451c-8c89-55ba378cca27/Untitled.png)
    

### **피처 간 상관관계 분석**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/709b60ac-d8fc-49a5-a26e-276c624d30de/Untitled.png)

대부분의 변수 사이에 약한 상관관계를 보이거나 상관관계가 거의 존재하지 않았다.

그 중에서 남유럽과 서유럽 사이에서 0.61, 동유럽과 서유럽 사이에서 0.58, 아프리카와 중동 사이에서 0.58, 남유럽과 동유럽 사이에서 0.57, 남유럽과 북미 사이에서 0.56, 서유럽과 북미 사이에서 0.54, 남미, 중남미와 중동사이에서 0.51의 양의 상관관계를 보였다.

**한국으로부터의 거리가 먼 국가들에 대한 관심도 변수 사이에서 상관관계가 존재하는 것으로 보임.**

### **모든 응답자 그룹별 관심도 평균 순위**

피벗테이블을 그려 1순위는 노란색으로 표시하여 한눈에 볼 수 있도록 함

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/207bba52-b007-46a8-9964-8c962b522fe5/Untitled.png)

### **군집분석**

사용자 특성에 따라 여행지를 추천하기 위해서는 우선적으로 군집화가 필요하다고 판단.

범주형 변수 데이터이므로 K-Modes 클러스터링을 진행하기로 함. 분석 진행 전 원핫인코딩을 통해 범주형 변수들을 수치화 해주었음.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/23dc02dd-2e31-4318-b9bc-8698da86dead/Untitled.png)

Elbow 기법에 따라 클러스터의 수는 5로 결정.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/b84947ae-0307-46f7-b787-c4185f987786/Untitled.png)

군집화 결과는 위와 같이 나왔으며 데이터셋에 클러스터 열을 추가해주었음.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/4a2e5fed-2d0b-4970-bcd8-09a6215f13ba/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/0215973e-cd1d-4296-be81-4fe126d81bfd/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/5cd156b6-6620-464d-9876-f22abe0e9095/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/b5ea47f0-3fae-4079-9ffd-77e935642365/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/f8659a16-c554-43da-86bd-c7702226ee6f/Untitled.png)

군집별 각 지역의 평균 관심도를 막대그래프로 시각화 하였으며 각 군집의 상위 3개 지역을 사용자에게 추천하기로 결정.

### **분류 모델 학습**

Decision Tree Classifier를 생성하여 사용자를 특성에 따라 분류하기로 결정.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/de016366-4897-4c55-a516-dc7c70d766d3/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/a8869c30-e634-44d3-8e04-778d56a79988/Untitled.png)

성별구분코드, 연령대구분명, 답변자거주지역명, 가구소득정도명 네가지 변수를 사용하여 모델 학습. test 데이터 사이즈는 0.2로 설정하여 학습 후 성능평가를 진행. accuracy 값이 **0.99**로 모델이 유효하다고 판단.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/0f432456-228c-4081-9cc1-e4ec288dd205/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/b74345f9-6441-4c82-a0e3-6386af36042b/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/9b5a7cbd-abe7-4de1-bf35-b88fb3a82d07/Untitled.png)

사용자 특성 정보를 입력 받고 예측한 군집을 이용하여 사용자가 관심가질만한 여행지역을 추천하는 알고리즘 작성.

### 크롤링 및 뷰 랜더링

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/1a9e30fd-03c5-4fbc-872d-97704e5046b0/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/188b7064-371e-47e1-acff-0257ca622c60/Untitled.png)

### Flask 웹 서비스 구현

![스크린샷 2024-05-16 오전 10.45.54.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/89c1eccb-bcc5-4338-a568-b4e63a036e5b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-05-16_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.45.54.png)

![스크린샷 2024-05-16 오전 11.45.48.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/117a59d7-819b-48d9-8c26-7cf049eb8738/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-05-16_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_11.45.48.png)

![스크린샷 2024-05-16 오전 11.54.27.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/665aabc8-73cb-4a4a-bcc8-48cc3d6fce43/1b3ec229-896f-48ea-a1fb-940232c96d5d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-05-16_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_11.54.27.png)
