from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.bubble import BubbleSort
from flask_app.models.insertSort import InserSort
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
    insert = InserSort()

    if session['sort'] == ("bubble"):
        bubble.bubbleSort(arr)

    elif session['sort'] == ("select"):
        select.selectionSort(arr)

    elif session['sort'] == ("insert"):
        insert.inserSort(arr)

    return redirect('/sorted')


@app.route('/sorted')
def sorted():
    print(session['originalArr'])
    return render_template("sorted-data.html", sort=session["sort"], arr=session["arr"], originalArr=session["originalArr"])