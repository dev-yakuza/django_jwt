## document
- [django_jwt 설명](#django_jwt-설명)
- [django_jwt説明](#django_jwt説明)
- [how to use django_jwt](#how-to-use-django_jwt)

## django_jwt 설명
django_jwt는 장고(django)에서 JWT(Json Web Token)을 사용하는 방법에 대해서 정리한 저장소(Repository)입니다. 이 저장소(Repository)를 제작하면서 작성한 블로그가 있습니다. 자세한 내용은 아래에 링크를 통해 확인하시기 바랍니다.

- [장고(django)에 JWT 사용하기](https://dev-yakuza.github.io/ko/django/jwt/)

### 사용 방법
아래에 명령어를 통해 django_jwt 저장소(Repository)를 복사(Clone)합니다.

```bash
git clone https://github.com/dev-yakuza/django_jwt.git
```

아래에 명령어로 파이썬 가상 환경을 생성합니다.

```bash
virtualenv venv
```

아래에 명령어로 파이썬 가상 환경을 실행합니다.

```bash
source venv/bin/activate
```

아래에 명령어로 프로젝트에 필요한 모듈을 설치합니다.

```bash
pip install -r requirements.txt
```

데이터베이스 연동을 위해 `django_jwt/settings.py`를 열고 아래의 내용을 자신의 DB에 맞게 수정합니다.

```python
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_jwt',  # DB name
        'USER': 'root',  # DB account
        'PASSWORD': '',  # DB account's password
        'HOST': '127.0.0.1',  # DB address(IP)
        'PORT': '3306',  # DB port(normally 3306)
    }
}
...
```

아래에 명령어로 데이터베이스를 생성합니다.

```bash
# python manage.py makemigrations
python manage.py migrate
```

아래에 명령어로 장고(django) 관리자를 생성합니다.

```bash
python manage.py createsuperuser
```

아래에 명령어로 준비한 데이터를 넣습니다.(Data Seed)

```bash
python manage.py loaddata blog/fixtures/posts-data.json
```

아래에 명령어로 테스트서버를 실행합니다.

```bash
python manage.py runserver
```

Postman을 실행 시키고 아래에 테스트 URL을 사용해 봅니다.

- JWT 토큰 발행
    - URL: http://localhost:8000/api/token/
    - Method: POST
    - Param: username, password
- JWT 토큰 검증
    - URL: http://localhost:8000/api/token/verify/
    - Method: POST
    - Param: token
- JWT 토큰 갱신
    - URL: http://localhost:8000/api/token/refresh/
    - Method: POST
    - Param: token
- JWT 인증을 이용한 정보 조회
    - URL: http://localhost:8000/api/blog/posts/
    - Method: GET
    - Header: Authorization jwt [jwt key]

자세한 테스트 방법은 아래의 블로그를 참고하시기 바랍니다.

- [장고(django)에 JWT 사용하기](https://dev-yakuza.github.io/ko/django/jwt/)


## django_jwt説明
django_jwtはジャンゴ(django)でJWT(Json Web Token)を使う方法について纏めたレポジトリ(Repository)です。このレポジトリ(Repository)を作る時作成したブログポストがあります。詳しく内容は下記のリンクを確認してください。

- [ジャンゴ(django)でJWTを使う方法](https://dev-yakuza.github.io/django/jwt/)

### 使い方
下記のコマンドでdjango_jwtレポジトリ(Repository)をコピー(Clone)します。

```bash
git clone https://github.com/dev-yakuza/django_jwt.git
```

下記のコマンドでパイソン仮想環境を作ります。

```bash
virtualenv venv
```

下記のコマンドでパイソンの仮想環境を実行します。

```bash
source venv/bin/activate
```

下記のコマンドでプロジェクトに必要なモジュールをインストールします。

```bash
pip install -r requirements.txt
```

データベースを連動するため、`django_jwt/settings.py`を開いて下記の内容を自分のDBに合わせて修正します。

```python
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_jwt',  # DB name
        'USER': 'root',  # DB account
        'PASSWORD': '',  # DB account's password
        'HOST': '127.0.0.1',  # DB address(IP)
        'PORT': '3306',  # DB port(normally 3306)
    }
}
...
```

下記のコマンドでデーターベースを生成します。

```bash
# python manage.py makemigrations
python manage.py migrate
```

下記のコマンドでジャンゴ(django)の管理者を生成します。

```bash
python manage.py createsuperuser
```

下記のコマンドで準備したデーターを入れます。(Data Seed)

```bash
python manage.py loaddata blog/fixtures/posts-data.json
```

下記のコマンドでテストサーバーを起動します。

```bash
python manage.py runserver
```

Postmanを実行して下記のテストURLを使ってみます。

- JWTトークン発行
    - URL: http://localhost:8000/api/token/
    - Method: POST
    - Param: username, password
- JWTトークン検証
    - URL: http://localhost:8000/api/token/verify/
    - Method: POST
    - Param: token
- JWTトークン更新
    - URL: http://localhost:8000/api/token/refresh/
    - Method: POST
    - Param: token
- JWT認証を使った情報取得
    - URL: http://localhost:8000/api/blog/posts/
    - Method: GET
    - Header: Authorization jwt [jwt key]

詳しくテスト方法は下記のブログを参考してください。

- [ジャンゴ(django)でJWTを使う方法](https://dev-yakuza.github.io/django/jwt/)

## how to use django_jwt
django_jwt is the repository about how to use JWT(Json Web Token) authentication in django. there are blog posts about this repository. if you want to know more details, see the link below.

- [Use JWT in django](https://dev-yakuza.github.io/en/django/jwt/)

### How to use
execute the command below to clone the django_jwt repository.

```bash
git clone https://github.com/dev-yakuza/django_jwt.git
```

execute the command below to start python virtual environment.

```bash
virtualenv venv
```

execute the command below to execute python virtual environment.

```bash
source venv/bin/activate
```

execute the command below to install modules for the project.

```bash
pip install -r requirements.txt
```

you need to modify `django_jwt/settings.py` to connect your database like below.

```python
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_jwt',  # DB name
        'USER': 'root',  # DB account
        'PASSWORD': '',  # DB account's password
        'HOST': '127.0.0.1',  # DB address(IP)
        'PORT': '3306',  # DB port(normally 3306)
    }
}
...
```

execute the command below to migrate.

```bash
# python manage.py makemigrations
python manage.py migrate
```

execute the command below to create django administrator.

```bash
python manage.py createsuperuser
```

execute the command below to insert data. (Data seed)

```bash
python manage.py loaddata blog/fixtures/posts-data.json
```

execute the command below to start django test server.

```bash
python manage.py runserver
```

open Postman and test links below.

- issue JWT token
    - URL: http://localhost:8000/api/token/
    - Method: POST
    - Param: username, password
- verify JWT token
    - URL: http://localhost:8000/api/token/verify/
    - Method: POST
    - Param: token
- refresh JWT token
    - URL: http://localhost:8000/api/token/refresh/
    - Method: POST
    - Param: token
- get the data with JWT authentication
    - URL: http://localhost:8000/api/blog/posts/
    - Method: GET
    - Header: Authorization jwt [jwt key]

you can see more details about test at the blog post below.

- [Use JWT in django](https://dev-yakuza.github.io/en/django/jwt/)