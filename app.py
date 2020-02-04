from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///URLS.db'

db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String)

    def __repr__(self):
        return '<URL %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conversion', methods=['POST'])
def conversion():
    long_url = request.form['input']
    new_url = URL(long_url = long_url)

    try:
        db.session.add(new_url)
        db.session.commit()
        return render_template('result.html', id=new_url.id)
    except:
        return "There was an error converting your URL"
