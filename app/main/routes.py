from app.main import bp
from flask import render_template, url_for, redirect, flash

from app.main.forms import AddRecetteForm, AddIngredientForm

@bp.route('/', methods=['GET','POST'])
@bp.route('/index', methods=['GET','POST'])
def index():
    return render_template('index.html')

@bp.route('/recettes')
def recettes():
    return render_template('recettes.html')

@bp.route('/recette/<recettename>')
def edit_recette(recettename):
    return render_template('recette.html')

@bp.route('/recette/newrecette', methods=['GET','POST'])
def add_recette():
    form = AddRecetteForm()
    if form.validate_on_submit():
        flash('Recette ajoutée !')
        return redirect(url_for('main.index'))
    return render_template('recette.html',form=form)

@bp.route('/planning')
def modify_planning():
    return render_template('planning.html')

@bp.route("/ingredient/newingredient", methods=['GET','POST'])
def add_ingredient():
    form = AddIngredientForm()
    if form.validate_on_submit():
        flash('Ingrédient ajouté !')
        return redirect(url_for('main.index'))
    return render_template('ingredient.html', form=form)


