from app import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    cost = db.Column(db.Integer, index=True, default=0)
    unite = db.Column(db.String(64), index=True)
    qte = db.Column(db.Integer)

    def set_cost(self, cost):
        self.cost = cost

    def set_qte(self, qte):
        self.qte = qte

class Recette(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), index=True, unique=True)
    cost = db.Column(db.Integer, index=True)
    ingredients = db.relationship('Ingredient', backref='ingredient', lazy='dynamic')

class Semaine(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer, index=True)
    jours = db.relationship('Jour', backref='jour', lazy='dynamic')

class Jour(db.Model):
    id = db.Column(db.Integeer, primary_key = True)
    midi = db.Column('')
    soir = db.Column('')

