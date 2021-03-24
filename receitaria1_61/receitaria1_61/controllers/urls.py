from typing import Dict
from flask import (
    Flask, render_template,
    url_for, request, flash,
    redirect, session
    )
from receitaria1_61 import app


class Usuarios:
    def __init__(self, id:int, apelido: str, nome:str, password:str) -> None:
        self.id = id
        self.apelido = apelido
        self.nome = nome
        self.password = password

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
    def __init__(self, id:int, nome: str, categoria: str, user: Usuarios, ingredientes: Dict, preparo:str) -> None:
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.user = user
        self.ingredientes = ingredientes
        self.preparo = preparo
    def __str__(self) -> str:
        return self.nome

user01 = Usuarios(1, 'pedro', 'Pedro Fernandes', 'senha')
user02 = Usuarios(2, 'irene', 'Irene Moraes', 'senha')
user03 = Usuarios(3, 'luna', 'Luna Maria', 'luna')
user04 = Usuarios(4, 'murphy', 'Murphy Aparecida', '1234')
users = {
    user01.apelido: user01,
    user02.apelido: user02,
    user03.apelido: user03,
    user04.apelido: user04
}
unidade01 = Unidades(1, 'gramas')
unidade02 = Unidades(2, 'colher(es)')
unidade03 = Unidades(3, 'copo(s)')
unidade04 = Unidades(4, 'unidade(s)')

lista_unidades = [unidade01, unidade02, unidade03, unidade04]

ingrediente01 = Ingredientes(1, 'farinha')
ingrediente02 = Ingredientes(2, 'chocolate')
ingrediente03 = Ingredientes(3, 'leite')
ingrediente04 = Ingredientes(4, 'cenoura')

lista_ingredientes = [ingrediente01, ingrediente02, ingrediente03, ingrediente04]

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

receita01 = Receitas(1, 'bolo_chocolate', 'sobremesa', user01, ingredientes_bolo_01, 'preparo bolo 01 chocolate')
receita02 = Receitas(2, 'bolo_cenoura', 'sobremesa', user02, ingredientes_bolo_02, 'preparo bolo 02 cenoura')
receita03 = Receitas(3, 'bolo_chocolate_01', 'sobremesa', user03, ingredientes_bolo_02, 'preparo bolo 03 chocolate tbm porem diferente')

lista_receitas = [receita01, receita02, receita03]

@app.route('/')
def index():
    return render_template ('index.html', titulo="Receitas", receitas=lista_receitas)   

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', titulo="Faça o seu Login", next=next)

@app.route('/ingredientes')
def ingredientes():
    return render_template ('ingredientes.html', titulo="Ingredientes Disponiveis", ingredientes=lista_ingredientes)

@app.route('/unidades')
def unidades():
    return render_template ('unidades.html', titulo="Unidades de Medida", unidades=lista_unidades)


@app.route('/auth', methods=['POST',])
def auth():
    if request.form['user'] in users:
        user = users[request.form['user']]
        if user.password == request.form['password']:
            session['user_logado'] = user.id
            flash(f'{user.nome} logou com sucesso!')
            next_pagina = request.form['next']
            return redirect(next_pagina)
        else:
            flash('Acesso incorreto')
            return redirect(url_for('login'))
    else:
        flash('Não logado, acesso incorreto')
        return redirect(url_for('login'))

@app.route('/novo')
def novo():
    return render_template ('novo.html', titulo="Nova Receita")

@app.route('/receita/<int:receita_id>')
def receita(receita_id):
    receita = lista_receitas[receita_id]
    return render_template ('receita.html', titulo="Receita", receita=receita)

@app.route('/logout')
def logout():
    session['user_logado'] = None
    flash('Nenhum usuário logado')
    return redirect(url_for('login'))