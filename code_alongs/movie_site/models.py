from flask import Flask
from flask_sqlalchemy import SQLAlchemy

'''
TODO:
setup .env
'''

# Configurations
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:5n9ws9iwd@127.0.0.1:3306/flask_db"
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),nullable=False, unique=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return "<User username=%s email=%s/>" % (self.username, self.email)
