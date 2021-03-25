from app import db

class Users(db.Model):
    __table__name = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    fullname = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)

    def __init__(self, id, username, fullname, password):
        self.id = id
        self.username = username
        self.fullname = fullname
        self.password = password

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    def __str__(self) -> str:
        return self.username

class Measures(db.Model):
    __table__name = 'mesures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self) -> str:
        return f'<Mesure {self.name}>'

    def __str__(self) -> str:
        return self.name

class Ingredients(db.Model):
    __table__name = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, id, name):
            self.id = id
            self.name = name

    def __repr__(self) -> str:
        return f'<Ingredients {self.name}>'

    def __str__(self) -> str:
        return self.name 

class IngredientsMesures(db.Model):
    __table__name = 'ingredients_mesures'
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey ('ingredients.id'), nullable=False)
    mesure_id = db.Column(db.Integer, db.ForeignKey ('mesures.id'), nullable=False)
    quantitie = db.Column(db.String(50), nullable=False)


class Prepare(db.Models):
    __table__name = 'prepare'
    id = db.Column(db.Integer, primary_key=True)
    step = db.Column(db.TextArea, nullable=False)


class Recipes (db.Model):
    __table__name = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    prepare_id = db.Column(db.Integer, db.ForeignKey ('prepare.id', nullable=False))
    user_id = db.Column(db.Integer, db.ForeignKey ('users.id'), nullable=False)
    ingredients_mesures_id = db.relationship('IngredientsMesures', foreign_keys=ingredients_mesures_id)

    def __init__(self, id, name, prepare, user_id, ingredients_mesures_id):
        self.id = id
        self.name = name
        self.prepare = name
        self.user_id = user_id
        self.ingredients_mesures_id = ingredients_mesures_id

    def __repr__(self) -> str:
        return f'<Recipe {self.name}>'

    def __str__(self) -> str:
        return self.name
