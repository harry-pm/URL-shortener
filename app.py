from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random_key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///URLS.db'

db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String)
    key = db.Column(db.String)

    def __repr__(self):
        return '<URL %r>' % self.id

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversion', methods=['POST'])
def conversion():
    long_url = request.form['input'].replace("http://", "")
    long_url = long_url.replace("https://", "")
    key = random_key.randomStringDigits(8)
    new_url = URL(long_url = long_url, key = key)

    try:
        db.session.add(new_url)
        db.session.commit()
        return render_template('result.html', key=new_url.key)
    except:
        return "There was an error converting your URL"

@app.route('/<key>', methods=['GET'])
def redirector(key):
    url = URL.query.filter(URL.key == key).first().long_url
    return redirect("http://" + url, code=302)

