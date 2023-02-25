## pythonic_chat
これはpythonの非同期通信になれるべく作成した練習用アプリ。
ajaxによる非同期通信についての学習もするべく実装をした.
また,HTMLなどの練習用としても用いた.
djangoのdockerによる環境構築を最初に行う.

参考:[https://www.python-izm.com/web/django/django_project/]
[https://python.keicode.com/django/]

## dockerによる環境構築

requirements.txtには仮想環境にインストールするライブラリを記載する.
dockerfileにはDockerイメージをビルドして実行するための命令を描く.
docker-compose.ymlにはアプリケーション実行に必要なコンテナの構造化されたデータを記載する.

参考:[https://qiita.com/mikako0115/items/6be7c40f24d2e6fabddb]「VSCode / WSL / DockerでDjangoの環境構築をしてみる【Window10, 11版】」
[https://zenn.dev/agepan/articles/docker-article-001]
[https://zenn.dev/masa20210102/articles/48775049baf8c4]
[https://book-reviews.blog/build-django-mysql-environment-with-docker-compose/]

その後にプロジェクト作成に移る.

ディレクトリが同期されるように,docker-compose.yml を書き換える前に、 必ず docker-compose をdocker-composeで終了させておきます。 終了する前に yml を書き換えてしまうと面倒なことになるようである.
***
`docker-compose down`
***

***
`docker-compose up -d`
***

この後にlocalhostに行ければ成功.

## DBの作成

dockerの拡張機能でコンテナを表示.
***
`mysql -u root -p`
***
でmysqlへログイン.
***
`show databases`
***

dbができていることを確認.
***
```python
+--------------------+
| Database           |
+--------------------+
| information_schema |
| django             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.04 sec)
```
参考資料:[https://qiita.com/bakupen/items/f23ce3d2325b4491a2dd]

## プロジェクトの作成方法
作成したいディレクトリ上で

`docker-compose run web django-admin startproject "chat_project" .`

を入力するとインストールされる.(この場合プロジェクト名はchat_project)

## アプリの作成方法
作成したいディレクトリ上で
***
`django-admin startapp <アプリケーション名>`
***

を入力するとインストールされる.(この場合chat_py)

## 開発のための仮想環境整備
***
`pip install virtualenv`
***
でvirtualenvをインストール。
***
`virtualenv env1`
***
を利用してenv1ファイルを作成.

pythonic_ajaxディレクトリに移動し,

***
`env1\Scripts\activate.bat`
***
を実行して仮想環境に切り替え.
仮想環境を終了するには、「deactivate」コマンドを実行する.
requiremenst.txt内に仮想環境にインストールするライブラリを記載.
***
```python
django
channels
channels-redis
```
***

のように記載する.そのあとに,

***
`python -m pip install -r requirements.txt`
***

を実行.環境が整備される.

***
`python -m pip freeze`
***

を利用してインストールされたものを確認.

参考:[https://qiita.com/t-iguchi/items/f9052d259cec7fe54a00]


## ディレクトリ構成について
***
|  ファイル名  |  役割  |
|  ----  |  ----  |
|  manage.py Django  |  プロジェクトの管理 用スクリプト  |
|  myapp1/__init__.py Python  |このディレクトリをパッケージとみなすためのファイル  |
|  myapp1/admin.py   |  管理ファイル  |
|  myapp1/apps.py  |  アプリケーション設定ファイル  |
|  myapp1/models.py  |データベース定義  |
|  myapp1/tests.py   |  テストコードを書くところ  |
|  myapp1/views.py  |  ビュー  |
***
初期状態では上のような構成になっている.
具体的には初期状態で以下のようになっている.

***
├── db.sqlite3
├── manage.py
├── chat_py(アプリ名)
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── pythonic_ajax(プロジェクト名)
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
***
プロジェクトとアプリは独立しているので最初に

`pythonic_ajax\\setting.py`
内にアプリ名を登録する必要がある.

## URL の設定
ディレクトリ chat_py 内に、次の内容でファイル urls.py を作成します。

***
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name='index'),
]
これを pythonic_ajax/urls.py から取り込む.

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('chat_py/', include('caht_py.urls')),
    url(r'^admin/', admin.site.urls),
]
```
***
このように URL の設定丸ごと取り込む仕組みがあるので、 chat_py アプリケーションに関わる URL については、 pythonic_ajax ディレクトリ内の urls.py に直接 URL を記述するのではなく、 chat_pyディレクトリ内の urls.py に記述しておくことができる.

## ルーティングについて
def 関数名(request):で定義
テンプレートを呼ぶ戻り値はrender関数
第1引数は受け取ったrequest
第2引数はテンプレートファイルのパス

## テンプレートの自動補完設定

htmlのようにemmetで補完を可能にするためにsetting.jsonファイルを書き換えて以下の行を追加した.

***
```js
"emmet.includeLanguages": {
    "django-html": "html",
},
```
***

参考:[https://tech-blog.cloud-config.jp/2020-05-20-vscode-emmet-not-html]

## テンプレートファイルのパスについて
TEMPLATESで設定したすべてのテンプレートディレクトリー下が一括して扱われる
テンプレートディレクトリー以下の相対パスとする

## viewの作成

pythonic_ajax/templateにchat_pyディレクトリを設定し,その中にchat.htmlを設定した.
変数などの利用方法は一部laravelと同様な部分がある.
変数は{{  }}で囲っておく.
viewの継承も可能である.

例)親テンプレート(共通の見た目)
***
```html
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta charset="UTF-8">
  <title>index.html</title>
  <style>
  body {
    background-color: #B2EBF2;
    font-family: sans-serif;
  }
  </style>
</head>
<body>
{% block content1 %} 

<!-- blockを定義してcontentという共通パーツを継承できるようにする. -->
{% endblock %}

</body>
</html>
```
***

子テンプレート(継承される独自のパーツを持つ部分)
***
```html
{% extends "myapp1/base.html" %}
<!-- extendsを最初に宣言して利用する親テンプレートを継承する. -->
{% block content1 %}
<h1>Hello, {{fname}}!</h1>

<!-- contentというblockに変数{{ fname }}を埋め込んでいる. -->

{% endblock %}
```
***
## modelについて

laravelと同様に,mvcアーキテクチャを使用して開発をする.

## staticディレクトリ
js用のディレクトリとcss用のディレクトリはここで管理する.

├── db.sqlite3
├── manage.py
├── chat_py(アプリ名)
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├──  pythonic_ajax(プロジェクト名)
│    ├── __init__.py
│    ├── settings.py
│    ├── urls.py
│    └── wsgi.py
└──static
      ├──css
      |    └── style.css
      └── js
          └── chat.js

のような構成となる.          


## マイグレーション
dbのカラムを決めてmysqlでdbを作成した.

カラムは以下のようにした.
users
|  カラム名  |  役割  |
|  ----  |  ----  |
|  id |  自動割り振り  |
|  user  |  ユーザー名  |
|  password   |  パスワード  |
|  email  |  メールアドレス  |

rooms
|  カラム名  |  役割  |
|  ----  |  ----  |
|  id |  自動割り振り  |
|  user  |  ユーザー名  |
|  room_name  |  ルーム名  |
|  room_id   |  部屋番号  |
|  describe   |  部屋の詳細  |
roomとuserは多対多のリレーションとする.

chats
|  カラム名  |  役割  |
|  ----  |  ----  |
|  content |  chatの内容  |
|  timestamp  |  作成日時  |

ユーザーとchatは1対多のリレーションとする.


