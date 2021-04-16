from app import db
from sqlalchemy import ForeignKey
from datetime import datetime

class User(db.Model):
    __table__name = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    fullname = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id, username, fullname, password):
        self.id = id
        self.username = username
        self.fullname = fullname
        self.password = password

    def __repr__(self) -> str:
        return f'<User {self.username}>'

    def __str__(self) -> str:
        return self.username

class Measure(db.Model):
    __table__name = 'mesures'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'<Mesure {self.name}>'

    def __str__(self) -> str:
        return self.name

class Ingredient(db.Model):
    __table__name = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id, name):
            self.id = id
            self.name = name

    def __repr__(self) -> str:
        return f'<Ingredients {self.name}>'

    def __str__(self) -> str:
        return self.name 

class RecipeIngredientMesure(db.Model):
    __table__name = 'recipe_ingredients_mesures'

    id = db.Column(db.Integer, primary_key=True)
    mesure_id = db.Column(db.Integer, db.ForeignKey ('mesure.id'), nullable=False)
    quantity = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    measure_id = db.Column(db.Integer, ForeignKey("measures.id", ondelete="RESTRICT"), nullable=False)
    ingredient_id = db.Column(db.Integer, ForeignKey("ingredients.id", ondelete="RESTRICT"), nullable=False)
    recipe_id = db.Column(db.Integer, ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False)

    measure = db.relationship("Measure", backref="recipe_ingredients_mesures")
    ingredient = db.relationship("Ingredient", backref="recipe_ingredients_mesures")

    def __repr__(self) -> str:
        return f'<RecipeIngredientMesure {self.id}>'

    def __str__(self) -> str:
        return self.id 

class Prepare(db.Models):
    __table__name = 'prepare'

    id = db.Column(db.Integer, primary_key=True)
    step = db.Column(db.TextArea, nullable=False)
    instruction = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    recipe_id = db.Column(db.Integer, ForeignKey("recipes.id", ondelete="CASCADE"))

    def __repr__(self):
        return f'<Prepare  {self.id}>'
    
    def __str__(self) -> str:
        return self.id 

class Recipe(db.Model):
    __table__name = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey ('users.id'), nullable=False)
    ingredients = db.relationship("Ingredient", backref="recipes", passive_deletes=True, passive_updates=True)
    prepare = db.relationship("Prepare", backref="recipes", passive_deletes=True, passive_updates=True)

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
