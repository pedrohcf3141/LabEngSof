from typing import Dict
from flask import (
    Flask, render_template
    )
app = Flask(__name__)
app.secret_key = "receitaria"


class Usuarios:
    def __init__(self, id:int, nome:str, senha:str) -> None:
        self.id = id
        self.nome = nome
        self.senha = senha

    def __str__(self) -> str:
        return self.nome


class Unidades:
    def __init__(self, id:int, nome:str,) -> None:
        self.id = id
        self.nome = nome
    def __str__(self) -> str:
        return self.nome


class Ingredientes:
    def __init__(self, id:int, nome:str,) -> None:
        self.id = id
        self.nome = nome
    def __str__(self) -> str:
        return self.nome


class Receitas:
    def __init__(self, id:int, nome: str, categoria: str, usuario: Usuarios, ingredientes: Dict, preparo:str) -> None:
        self.nome = nome
        self.categoria = categoria
        self.usuario = usuario
        self.ingredientes = ingredientes
        self.preparo = preparo
    def __str__(self) -> str:
        return self.nome

usuario01 = Usuarios(1, 'Pedro Fernandes', 'senha')
usuario02 = Usuarios(2, 'Irene Moraes', 'senha')
usuario03 = Usuarios(3, 'Luna Maria', 'luna')
usuario04 = Usuarios(4, 'Murphy Aparecida', '1234')
usuarios = {
    usuario01.id: usuario01,
    usuario02.id: usuario02,
    usuario03.id: usuario03,
    usuario04.id: usuario04
}
unidade01 = Unidades(1, 'gramas')
unidade02 = Unidades(2, 'colher(es)')
unidade03 = Unidades(3, 'copo(s)')
unidade04 = Unidades(4, 'unidade(s)')

ingrediente01 = Ingredientes(1, 'farinha')
ingrediente02 = Ingredientes(2, 'chocolate')
ingrediente03 = Ingredientes(3, 'leite')
ingrediente04 = Ingredientes(4, 'cenoura')

ingredientes_bolo_01 = {
    ingrediente01.nome:('200', unidade01),
    ingrediente02.nome:('10', unidade02),
    ingrediente03.nome:('2', unidade03)
}
ingredientes_bolo_02 = {
    ingrediente01.nome:('200', unidade01),
    ingrediente02.nome:('10', unidade02),
    ingrediente04.nome:('2', unidade04)
}

receita01 = Receitas(1, 'bolo_chocolate', 'sobremesa', usuario01, ingredientes_bolo_01, 'preparo bolo 01 chocolate')
receita02 = Receitas(2, 'bolo_cenoura', 'sobremesa', usuario02, ingredientes_bolo_02, 'preparo bolo 02 cenoura')
receita03 = Receitas(3, 'bolo_chocolate_01', 'sobremesa', usuario03, ingredientes_bolo_02, 'preparo bolo 03 chocolate tbm porem diferente')

lista_receitas = [receita01, receita02, receita03]

@app.route('/')
def index():
    return render_template ('index.html', titulo="Receitas", receitas=lista_receitas)

app.run(debug=True)