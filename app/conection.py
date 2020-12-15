from flask import Flask
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = '192.168.0.7'
app.config['MYSQL_USER'] = 'iago'
app.config['MYSQL_PASSWORD'] = 'iago'
app.config['MYSQL_DB'] = 'safemeet'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
