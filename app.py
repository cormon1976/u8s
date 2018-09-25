import os
from functools import wraps
from flask import Flask
from flask import render_template
from flask import Flask, redirect, render_template, flash, request, session, url_for
from flask_wtf import Form
from wtforms.fields import StringField, SubmitField

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/links")
def links():
    return render_template('index.html')


@app.route("/schedule")
def schedule():
    return render_template('index.html')

@app.route("/base")
def base():
    return render_template('base.html')

@app.route("/sample")
def sample():
    return render_template('training_plans/sample.html')


if __name__ == "__main__":
    app.run(debug=True)


