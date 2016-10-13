from flask import Flask
from pip._vendor import requests
app = Flask(__name__)

fila =[]
@app.route('/')
def fila(add):
    return fila.append(add)
