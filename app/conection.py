from flask import Flask
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'agfmsql'
app.config['MYSQL_DB'] = 'safemeet'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)