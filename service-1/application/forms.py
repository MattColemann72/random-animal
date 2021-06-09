from flask_wtf import FlaskForm
from wtforms import SubmitField

class GenerateAnimal(FlaskForm):
    submit = SubmitField('Generate Animal')