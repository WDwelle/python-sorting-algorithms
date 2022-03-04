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
    data = {
        "sort" : request.form.get("sorts")
    }

    arr = [10, 65, 12, 1, 7, 69, 85, 11, 15, 42]

    bubble = BubbleSort()
    select = SelectSort()

    if data == ("bubble"):
        print("unsorted array:")
        print(arr)

        print("sorted array:")
        bubble.bubbleSort(arr)
        print(arr)

    elif data == ("select"):
        print("unsorted array:")
        print(arr)

        print("sorted array:")
        select.selectionSort(arr)
        print(arr)

    return redirect('/sorted')


@app.route('/sorted')
def sorted():

    return render_template("sorted-data.html")