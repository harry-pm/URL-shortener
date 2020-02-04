from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///URLS.db'

db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # add columns to model here
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<URL %r>' % self.id

@app.route('/')
def index():
    return "sup B Ting"

