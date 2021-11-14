from app.main import bp
from flask import render_template

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
    return render_template('recette.html')

@bp.route('/planning')
def modify_planning():
    return render_template('planning.html')


