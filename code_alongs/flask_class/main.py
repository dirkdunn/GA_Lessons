from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:5n9ws9iwd@127.0.0.1:3306/flask_db"
db=SQLAlchemy(app)

class Users(db.Model):
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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_person', methods=['POST'])
def add_person():
    new_user = Users(request.form['first_name'], request.form['last_name'], request.form['age'])
    db.session.add(new_user)
    db.session.commit()
    return "person added."


if __name__ == "__main__":
    app.run(debug=True)
