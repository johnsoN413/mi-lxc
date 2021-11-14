from app.main import bp
from flask import render_template, url_for, redirect

from app.main.forms import AddRecette

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

@bp.route('/recette/newrecette')
def add_recette():
    form = AddRecette()
    if form.validate_on_submit():
        flash('Recette ajoutée !')
        return redirect(url_for('main.index'))
    return render_template('recette.html',form=form)

@bp.route('/planning')
def modify_planning():
    return render_template('planning.html')


