from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import secrets


my_secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = my_secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
db = SQLAlchemy(app)
