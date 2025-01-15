# README

# 게임추천사이트

##### OPENAI 기반의 챗봇과 로그인/회원가입 기능을 통해 게임을 추천하는 웹 애플리케이션입니다.
##### 프로젝트의 이름은 MANGO입니다.

### 주요 기능
* 회원가입 및 회원기능 : 새로운 사용자는 회원가입을 한 후 기능을 이용하실 수 있습니다. 비회원일 경우 사용할 수 있는 기능이 제한적입니다.
* 게임 추천 : 사용자의 취향을 도출해 메인페이지에 투영합니다.
* 직관적인 UI: 사용자가 손쉽게 접근하고 사용할 수 있는 간단한 인터페이스 제공.


### 기술 스택
* 프론트엔드: streamlit
* 백엔드: Django
* 데이터베이스: sqlite
* AI 챗봇: OpenAI API
* 인증: JWT 또는 OAuth 2.0



### 설치 및 실행 방법
#### 1. 프로젝트 클론
```
git clone https://github.com/MANGO-SP/Indie_Mango.git
cd indie_mango
```
#### 2. 필수 설치
```
pip install -r requirements.txt

```
#### 3. 환경 변수 설정
```.env```파일을 생성하고 아래의 내용을 추가하세요.
```
OPENAI_API_KEY=your_openai_api_key

```
#### 4. 서버 실행
```
streamlit run indie_mango.py
```
이후 브라우저에서 ```http://localhost:8000```에 접속합니다.

### 사용 방법
1. 회원가입 후 로그인하세요.
2. 챗봇과 대화를 통해 몰랐던 게임들을 확인해보세요.
3. 추천된 게임을 확인하고 즐기세요.

### 프로젝트 구조
```
Indie_Mango/
├── chatbot/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── chatbot.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── games/
│   ├── management/commeands/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── indie_mango/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── .gitignore
├── README.md
├── dockerfile
├── manage.py
├── requirements.txt

```
