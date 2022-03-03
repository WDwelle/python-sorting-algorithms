from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.bubble import BubbleSort
from flask_app.models.selectionSort import SelectSort


@app.route('/')
def hello():
    return render_template('index.html')