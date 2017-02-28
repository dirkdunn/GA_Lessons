from flask import Flask, render_template, request, redirect, url_for
from models import db, User
from sqlalchemy.exc import IntegrityError
import requests


app = Flask(__name__)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/hipster')
def hipster():
    r = requests.get('http://hipsterjesus.com/api')
    # print r.json()
    return r.json()['text']

@app.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    if user != None:
        return render_template('profile.html',user=user)
    else:
        return redirect(url_for('index'))

@app.route('/post_user', methods=['POST'])
def post_user():
    users = User.query.all()
    user = User(request.form['un'], request.form['em'])
    try:
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    except IntegrityError:
        # we have to reset the session otherwise it just gets clogged and never committed because of the DB error
        db.session.rollback()
        return render_template('index.html',integError="Woops! looks like that username or email is already taken!", users=users)

if __name__ == '__main__':
    app.run(debug=True)
