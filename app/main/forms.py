from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloadField, FieldList, IntegerField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Length

class AddIngredientForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()])
    cost = FloatField('Coût',default=0.0)
    submit = SubmitField('Ajouter')

class AddRecetteForm(FlaskForm):
    name = StringField('Nom', validators = [DataRequired()])
    ingredients = SelectMultipleField("Ingrédients", choices=[("Carottes"),("Poivrons"),("Tomate")])
    submit = SubmitField("Terminer la recette")
