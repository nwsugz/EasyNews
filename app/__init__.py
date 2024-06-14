from flask import Flask

#app = Flask(__name__)

from fastapi import FastAPI

app = FastAPI()

from app import routes