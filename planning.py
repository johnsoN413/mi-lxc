from app import create_app, db
from app.models import Ingredient, Recette, Relation

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Ingredient": Ingredient, "Recette": Recette, "Relation": Relation}
