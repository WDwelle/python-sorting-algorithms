# -*- coding: UTF-8 -*-
from flask_app.controllers import sorting
#from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
app.secret_key = "you were my brother, Anakin"

if __name__ == "__main__":
    app.run(host='0.0.0.0')