#!/usr/bin/env python

# app.py

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello():
      return 'world'

@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }

    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
