from typing import Dict
from flask import (
    Flask, render_template,
    url_for, request, flash,
    redirect, session
    )
from receitaria1_61 import app
class Usuarios:
    def __init__(self, id:int, apelido: str, nome:str, senha:str) -> None:
        self.id = id
        self.apelido = apelido
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

usuario01 = Usuarios(1, 'pedro', 'Pedro Fernandes', 'senha')
usuario02 = Usuarios(2, 'irene', 'Irene Moraes', 'senha')
usuario03 = Usuarios(3, 'luna', 'Luna Maria', 'luna')
usuario04 = Usuarios(4, 'murphy', 'Murphy Aparecida', '1234')
usuarios = {
    usuario01.apelido: usuario01,
    usuario02.apelido: usuario02,
    usuario03.apelido: usuario03,
    usuario04.apelido: usuario04
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

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo="Faça o seu Login", proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(f'{usuario.nome} logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
        else:
            flash('Acesso incorreto')
            return redirect(url_for('login'))
    else:
        flash('Não logado, acesso incorreto')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado')
    return redirect(url_for('login'))