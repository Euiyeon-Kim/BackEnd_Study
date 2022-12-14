# 목차

1. [Chapter 1~2 - 프로젝트 시작하는 법](#chapter-1-chapter-2)
2. [Chapter 3 - 장고 기본 소개](#chapter-3)
3. [Chapter 4 - App 생성하기](#chapter-4)
4. [Week5](#chapter-5)

-   [ETC](#etc)

# Chapter 1 Chapter 2

## Environment Setting

장고 공식 홈페이지에서도 각 프로젝트마다 환경 따로 관리할 것 추천

```bash
    poetry init
    poetry shell
    poetry add django
    exit
```

## Start project

create-react-app이랑 비슷

```bash
    django-admin startproject config .    # 현재 폴더에 프로젝트 생성
    python manage.py migrate              # 데이터 베이스 연동
    python manage.py runserver            # 서버 시작
```

## DJango

-   Support DB migration
-   Use SQlite DB

# Chapter 3

## Admin 패널 사용하기

아래 명령어로 관리자 계정 생성 후 서버주소/admin 접속시 admin 패널 사용 가능

```bash
    python manage.py createsuperuser
```

## Django Applications

장고로 백엔드를 구성하기 위해서는 사용할 데이터와 기능을 나눠줘야함
장고에서는 이 데이터랑 데이터 처리 로직 조합을 app이라고 부르고, app들 간에는 소통도 가능함

# Chapter 4

## Application 생성하기

아래 명령어를 입력하면 필수 파일들이 생성됨

```bash
    python manage.py startapp AppName
```

새로 생긴 AppName 폴더에서 작업을 마치고 setting.py의 INSTALLED_APPS에 새로 생긴 앱을 추가해주면 새로 생긴 App과 함께 서버 동작

-   models.py : 데이터의 형태를 알려주는 파일

    아래와 같은 방식으로 데이터 타입 및 옵션 지정 가능

    ```python
        class House(models.Model):
            name = models.CharField(max_length=140)
            price = models.PositiveIntegerField()
            description = models.TextField()
            address = models.CharField(verbose_name="주소", max_length=140, help_text="도로명주소로 작성하시오")

    ```

-   admin.py : 기본적으로 제공되는 user admin 패널의 형태로 데이터를 관리할 수 있도록 구현하는 파일
    ```python
        @admin.register(House)      #admin으로 House 모델을 control할 것이라고 알려주는 decorator
        class HouseAdmin(admin.ModelAdmin):
            pass
    ```

위 같은 작업을 하고 나면, 실제 DB 테이블을 만들고 데이터를 관리하는 migration 기능이 필요한데, 아래 명령어를 통해 initialize 가능

```bash
    python manage.py makemigrations     # 장고 코드와 DB 연동 코드 생성
    python manage.py migrate            # 연동
```

## Admin 기능 추가하기

-   admin으로 들어갔을 때 보이는 이름 수정
    ```python
        # AppName/models.py에 다음 method 추가하기
        def __str__(self):
            return self.name
    ```
-   admin으로 들어갔을 때 property 바로 보기, 검색 및 필터하기

    ```python
        # AppName/admin.py에 다음 변수 설정하기
        list_display = ('name', 'price', 'address', 'pet_allowed')
        list_filter = ('price', 'pet_allowed')
        search_fields = ('address')
        # 'address__startswith'등으로 검색 옵션도 지정 가능
    ```

# Week 5

## Customize User

[Docs](#https://docs.djangoproject.com/ko/4.1/topics/auth/customizing/)

# ETC

## OOP

-   Encapsulation
-   Inheritance
-   Abstraction
-   Polymorphism

## More function about Django

-   config/settings.py 에 TIMEZONE & LANGUAGE_CODE 설정 가능
-   config/urls.py 에서 url path 관리 가능

## Deploy Server

-   runserver 커맨드로 빌드되는 서버는 개발용으로 성능 및 보안이 검증된 서버가 아님

## Framework vs Library

-   Framework is looking for my code and use or call or do whatever they need
-   I import library and use it by myself
