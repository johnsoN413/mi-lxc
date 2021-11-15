from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import ValidationError, DataRequired

class AddIngredientForm(FlaskForm):
    name = StringField('Nom', validators = [DataRequired()])
    cost = FloatField('Coût',default=0.0)
    submit = SubmitField('Ajouter')

class AddRecetteForm(FlaskForm):
    name = StringField('Nom', validators = [DataRequired()])
    ingredients = StringField("Ingrédients")
    submit = SubmitField("Terminer la recette")
