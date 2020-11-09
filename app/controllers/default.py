#from flask import render_template

from flask import render_template

from app import app

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html'), 200

@app.route("/cadastro_doenca")
def cadastro_doenca():
    return 'Olá doenca!'