# 가상환경 만들기

Virtualenv , venv 중에 venv를 사용한다.

python -m venv venv
venv\Scripts\activate
source venv/bin/activate
deactivate

- pip Update 는 필수로 한다. (python.exe -m pip install --upgrade pip)

# 패키지 설치 방법

- requirements.txt가 있는경우
  - pip install -r requirements.txt
- 수동설치시
  - pip install  packagename [pandas]
- 패키지 설치시
  - pip install -r requirements.txt
- pip list (requrements.txt 생성)
  - pip freeze > requirements.txt

# App실행 
uvicorn app.main:app --host 0.0.0.0 --port 8000
uvicorn app.main:app --reload

http://127.0.0.1:8000/docs

# 비교 사항

아래는 `virtualenv`와 `venv`의 주요 장단점을 비교한 표입니다.

물론, 아래는 `virtualenv`와 `venv`의 각각의 장단점을 비교한 Markdown 형식의 표입니다.

| 특성                | virtualenv                                              | venv                                                 |
| ------------------- | ------------------------------------------------------- | ---------------------------------------------------- |
| 개발사              | 독립적 프로젝트                                         | 파이썬 표준 라이브러리 내장 모듈                     |
| Python 버전 지원    | 파이썬 2 및 3 모두 지원                                 | 파이썬 3.3 이상 지원                                 |
| 가상 환경 분리 방식 | 시스템 파이썬 인터프리터를 기반으로 생성                | 자체 파이썬 인터프리터를 가상 환경 내에서 생성       |
| 특별한 기능         | 다양한 파이썬 버전 간 라이브러리 공유 등 추가 기능 제공 | 간단한 사용 및 관리를 위한 설계로 제한적인 기능 제공 |
| 성능                | 일반적으로 `venv`보다 성능이 좋을 수 있음             | `virtualenv`보다 더 나은 성능 제공 가능성 있음     |

이 표를 통해 각각의 도구가 가지는 장점과 한계를 더 잘 이해하실 수 있을 것입니다.
