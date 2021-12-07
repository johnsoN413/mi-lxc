from app import db

class Relation(db.Model):
    recette_id = db.Column(db.ForeignKey('recette.id'), primary_key=True)
    ingredient_id = db.Column(db.ForeignKey('ingredient.id'), primary_key=True)
    qte_necessaire = db.Column(db.Integer)
    qte_achat = db.Column(db.Integer)
    recette = db.relationship("Recette", back_populates="ingredients")
    ingredient = db.relationship("Ingredient", back_populates="recettes")

    def set_qte_necessaire(self, qte) :
        self.qte = qte

    def set_qte_achat(self) :
        qte_achat = self.ingredient.qte
        qte_necessaire = self.qte_necessaire
        while qte_achat < qte_necessaire :
            qte_achat += self.ingredient.qte
        self.qte_achat = qte_achat


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    cost = db.Column(db.Integer, index=True, default=0)
    unite = db.Column(db.String(64), index=True)
    qte = db.Column(db.Integer)
    recettes = db.relationship("Relation", back_populates="ingredient")

    def set_cost(self, cost):
        self.cost = cost

    def set_qte(self, qte):
        self.qte = qte

class Recette(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index=True, unique=True)
    cost = db.Column(db.Integer, index=True)
    ingredients = db.relationship("Relation", back_populates="recette")

    def set_cost(self) :
        cost = 0
        for ingredient in self.ingredients :
            cost += (ingredient.qte_achat/ingredient.ingredient.qte)*ingredient.ingredient.cost
        self.cost = cost


'''
class Semaine(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer, index=True)
    jours = db.relationship('Jour', backref='jour', lazy='dynamic')

class Jour(db.Model):
    id = db.Column(db.Integeer, primary_key = True)
    midi = db.Column('')
    soir = db.Column('')
'''
