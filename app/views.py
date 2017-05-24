from flask import render_template

from app import app

@app.route('/')
def hello_sari():
    return('Hello Sari!')
