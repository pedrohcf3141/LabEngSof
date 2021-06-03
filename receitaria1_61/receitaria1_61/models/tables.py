from receitaria1_61.db import db
from sqlalchemy import ForeignKey
from datetime import datetime

class ReceitaInstrucao(db.Model):
    __tablename__ = "receita_instrucoes"

    id = db.Column(db.Integer, primary_key=True)
    instruction = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    receita_id = db.Column(db.Integer, ForeignKey("receitas.id", ondelete="CASCADE"))

    def __repr__(self):
        return "<ReceitaInstrucao %r>" % self.id

class ReceitaIngrediente(db.Model):
    __tablename__ = "receitas_ingredientes"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    unidade_id = db.Column(db.Integer, ForeignKey("unidades.id", ondelete="RESTRICT"), nullable=False)
    ingrediente_id = db.Column(db.Integer, ForeignKey("ingredientes.id", ondelete="RESTRICT"), nullable=False)
    receita_id = db.Column(db.Integer, ForeignKey("receitas.id", ondelete="CASCADE"), nullable=False)

    unidade = db.relationship("Unidade", backref="receitas_ingredientes")
    ingrediente = db.relationship("Ingrediente", backref="receitas_ingredientes")

    def __repr__(self):
        return "<ReceitaIngrediente %r>" % self.id

class Receita(db.Model):
    __tablename__ = "receitas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    ingredientes = db.relationship("ReceitaIngrediente", backref="receitas", passive_deletes=True, passive_updates=True)
    instructions = db.relationship("ReceitaInstrucao", backref="receitas", passive_deletes=True, passive_updates=True)

    def __repr__(self):
        return "<Receita %r>" % self.id

class Ingrediente(db.Model):
    __tablename__ = "ingredientes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Ingrediente %r>" % self.id

class Unidade(db.Model):
    __tablename__ = "unidades"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Unidade %r>" % self.id
