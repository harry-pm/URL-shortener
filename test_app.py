import pytest
from flask import Flask
from app import app, db, URL

def test_basic_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>URL shortener</h1>' in response.data

def test_post_route_success():
    client = app.test_client()
    response = client.post('/conversion', data=dict(input="http://google.com"))
    assert response.status_code == 200
    assert b"</a>" in response.data

def test_post_route_failure():
    client = app.test_client()
    response = client.post('/conversion', data=dict(input="http://jklasdfjawe"))
    assert response.status_code == 200
    assert b"<p>This URL is not valid</p>" in response.data

def test_database_entry():
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True
    db.create_all()
    url = URL()
    db.session.add(url)
    db.session.commit()
    assert url in db.session
    db.session.remove()
    db.drop_all()