#from flask import render_template

from flask import render_template, redirect, url_for

from app import app, db

from app.models.forms import DoencaForm, DadoEpidemiologicoForm
from app.models.tables import Doenca, DadoEpidemiologico

@app.route("/index")
@app.route("/")
def index():
    epidemias = DadoEpidemiologico.query.order_by(DadoEpidemiologico.id).all()
    return render_template('index.html', epidemias=epidemias), 200

#@app.route('/visualizar_doencas/<id>')
@app.route('/visualizar_doencas') #defaults={ id: None })
def visualizar_doencas():
    doencas = Doenca.query.order_by(Doenca.id).all()
    return render_template('doencas_list.html', doencas=doencas)

@app.route("/cadastro_doenca", methods=["POST", "GET"])
def cadastro_doenca():
    form = DoencaForm()

    if form.validate_on_submit():
        doenca = Doenca(form.nome.data, form.sintomas.data)
        db.session.add(doenca)
        db.session.commit()
        return  redirect(url_for('visualizar_doencas'))

    return render_template('doenca_form.html', form=form)

@app.route("/cadastro_dado_epidemiologico", methods=["POST", "GET"])
def cadastro_dado_epidemiologico():
    doencas = Doenca.query.order_by(Doenca.id).all()
    form = DadoEpidemiologicoForm(doencas)

    if form.validate_on_submit():
        dado_epid = DadoEpidemiologico(form.data_coleta.data, form.doenca_associada.data)
        db.session.add(dado_epid)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('dadoepidemiologico_form.html', doencas=doencas, form=form)
