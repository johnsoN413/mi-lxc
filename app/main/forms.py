from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, FieldList
from wtforms.validators import ValidationError, DataRequired, Length

class AddIngredientForm(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()])
    cost = DecimalField('Coût',default=0.0)
    submit = SubmitField('Ajouter')

class AddRecette(FlaskForm):
    name = StringField('Nom', validators = [DataRequired()])
    ingredients = FieldList(StringField('Ingredient', validators=[DataRequired()]))
    submit = SubmitField("Terminer la recette")
