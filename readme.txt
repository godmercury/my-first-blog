참조URL : https://tutorial.djangogirls.org/ko/



설치된 패키지 리스트 보기
pip list


가상환경 설치 (환경별로 패키지의 버전이 다르게 관리 가능)
python -m venv myvenv

가상환경 실행 (한 머신에 한 개의 가상환경만 실행 가능)
myvenv\Scripts\activate
(myvenv) 이렇게 나오면 가상환경 활성화

deactivate 활성화 종료



***************************************
가상 환경에서 실행


장고 설치
pip install django


장고 프로젝트 설치
django-admin startproject 프로젝트명 .


장고 프로젝트 설치 후 자동으로 생기는 파일
manage.py : 사이트 관리를 도와주는 역할(모든 장고 명령을 이 파일을 통해 실행). 이 스크립트로 다른 설치 없

이 컴퓨터에서 웹 서버를 시작할 수 있다.
프로젝트폴더
	- __init__.py
	- asgi.py
	- settings.py : 웹사이트 설정이 있는 파일 (언어, 타임존, 디비설정파일 등)
	- urls.py
	- wsgi.py
# 참조 URL : https://docs.djangoproject.com/ko/3.1/intro/tutorial01/


디비 생성한건가?
python manage.py migrate

서버 실행
python manage.py runserver

장고 앱 만들기
python manage.py startapp blog
* 앱을 만든 후 setting.py의 INSTALLED_APPS에 경로를 추가해야 함!


테이블 명세서 만들기
python manage.py makemigrations blog


테이블 만들기
python manage.py migrate blog


슈퍼유저 만들기
python manage.py createsuperuser


쉘 접속
python manage.py shell


쉘에서 파이선 명령어 쓸 때 좀 더 편리하게 쓰는 툴
pip install ipython


개발 서버 시작
python manage.py runserver


***************************************
강의 URL
https://tutorial.djangogirls.org/ko/


vscode에서 파이선 실행하기

https://yiunsr.tistory.com/837

python.pythonPath 경로대로 virtualenv 를 설정하기 위해서는 ctrl+shitf+P 를 누른 후, python select

interprenter 를 선택한 후 해당 경로대로 python 을 선택하면 된다. python.pythonPath 를 넣지않고 하면 해당

경로 자체가 뜨지 않는다.



장고 문서
https://docs.djangoproject.com/
