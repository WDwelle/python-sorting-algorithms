from flask_app.controllers import sorts
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


arr = [10, 65, 12, 1, 7, 69, 85, 11, 15, 42]

bubble = BubbleSort()
select = SelectSort()


#sort = input("which sort would you like to use (type: bubble or select)?")


# if sort == ("bubble"):
#     print("unsorted array:")
#     print(arr)

#     print("sorted array:")
#     bubble.bubbleSort(arr)
#     print(arr)

# elif sort == ("select"):
#     print("unsorted array:")
#     print(arr)

#     print("sorted array:")
#     select.selectionSort(arr)
#     print(arr)


if __name__ == "__main__":
    app.run(debug=True)