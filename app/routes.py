from app import app
from flask import render_template

@app.get("/hello")
def hello():
    return {"message": "안녕하세요 파이보"}