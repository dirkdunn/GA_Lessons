from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy(app)

class User(db.Model):
    __tablename__="flask_db_table"
    id= db.Column(db.Integer,primary_key=True)
    first_name= db.Column(db.String(45), nullable=False)
    last_name= db.Column(db.String(45), nullable=False)
    age= db.Column(db.Integer, nullable=False)

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return "<User %s %s %d>" % (self.first_name, self.last_name, self.age)

# db.create_all()
