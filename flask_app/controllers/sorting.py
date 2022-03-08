# -*- coding: UTF-8 -*-
from email.mime import base
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.bubble import BubbleSort
from flask_app.models.selectionSort import SelectSort

#Home
@app.route('/')
def index():
    return render_template('index.html')

#Submit and sort data
@app.route('/submit', methods = ["POST"])
def sort():

    arr = []
    data = request.form.get("arrValues")
    nums = data.split(',')
    arr = [int(num) for num in nums]
    originalArr = []
    data = request.form.get("arrValues")
    nums = data.split(',')
    originalArr = [int(num) for num in nums]
    session["originalArr"] = originalArr
    session["arr"] = arr
    session["sort"] = request.form.get("sorts")

    bubble = BubbleSort()
    select = SelectSort()

    if session['sort'] == ("bubble"):
        #print("unsorted array:")
        #print(arr)
        #print(session["originalArr"])

        #print("sorted array:")
        bubble.bubbleSort(arr)
        #print(arr)

    elif session['sort'] == ("select"):
        #print("unsorted array:")
        #print(arr)
        #print(session["originalArr"])

        #print("sorted array:")
        select.selectionSort(arr)
        #print(arr)

    return redirect('/sorted')


@app.route('/sorted')
def sorted():
    #print(session['originalArr'])
    return render_template("sorted-data.html", sort=session["sort"], arr=session["arr"], originalArr=session["originalArr"])