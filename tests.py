import unittest
from app import create_app, db
from app.models import Ingredient, Recette, Relation
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
    ELASTICSEARCH_URL = None

class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_qte_achat(self):
        recette = Recette(name="recette")
        salade = Ingredient(name="salade", cost=5, unite="unite", qte=3)
        tomate = Ingredient(name="tomate", cost=1, unite="unite", qte=1)
        rel_salade = Relation(qte_necessaire=1)
        rel_tomate = Relation(qte_necessaire=4)
        rel_salade.ingredient = salade
        rel_tomate.ingredient = tomate
        rel_salade.set_qte_achat()
        rel_tomate.set_qte_achat()
        self.assertTrue(rel_salade.qte_achat==3)
        self.assertTrue(rel_tomate.qte_achat==4)

    def test_cost_recette(self):
        recette = Recette(name="recette")
        salade = Ingredient(name="salade", cost=5, unite="unite", qte=3)
        tomate = Ingredient(name="tomate", cost=1, unite="unite", qte=1)
        rel_salade = Relation(qte_necessaire=1)
        rel_tomate = Relation(qte_necessaire=4)
        rel_salade.ingredient = salade
        rel_tomate.ingredient = tomate
        rel_salade.set_qte_achat()
        rel_tomate.set_qte_achat()
        recette.ingredients.append(rel_salade)
        recette.ingredients.append(rel_tomate)
        recette.set_cost()
        self.assertTrue(recette.cost==9)

if __name__ == '__main__':
    unittest.main(verbosity=2)
