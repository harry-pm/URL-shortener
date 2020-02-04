from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///URLS.db'

db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String)
    short_url = db.Column(db.String)

    def __repr__(self):
        return '<URL %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversion', methods=['POST'])
def conversion():
    return 'new url!'
