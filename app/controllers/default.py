#from flask import render_template

from run import app


@app.route("/")
def index():
    return 'Hello world!'