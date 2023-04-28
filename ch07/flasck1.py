# flask 웹 프로임워크 사용하기
import flask
from flask import Flask

app = Flask(__name__)

#route() 경로를 바꿔줌
@app.route('/') # 127.0.0.1:500/
def index():
    return "<h1>Hello~ flask!</h1>"

@app.route('/login') # 127.0.0.1:500/login
def login():
    return "<h1>로그인 페이지 입니다.</h1>"

@app.route('/board/view') # 127.0.0.1:500/board/view
def detail():
    return "<h1>게시판 상세 페이지</h1>"

app.run() # 서버 실행