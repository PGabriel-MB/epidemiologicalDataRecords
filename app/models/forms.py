from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import DateField
from wtforms import SelectField
from wtforms.validators import DataRequired

class DoencaForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    sintomas = TextAreaField('sintomas', validators=[DataRequired()])

class DadoEpidemiologicoForm(FlaskForm):
    data_coleta = DateField('data_coleta', validators=[DataRequired()])
    doenca_associada = SelectField('data_coleta', validators=[DataRequired()], choices=[], coerce=int)

    def __init__(self, doencas_associadas=None):
        super().__init__()
        if doencas_associadas:
            self.doenca_associada.choices = [(doenca.id, doenca.nome) for doenca in doencas_associadas]
            

