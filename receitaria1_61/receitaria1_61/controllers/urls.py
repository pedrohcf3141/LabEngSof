from typing import Dict
from receitaria1_61.db import db
from flask import (
    Flask, render_template,
    url_for, request, flash,
    redirect, session
    )
from receitaria1_61 import app
from receitaria1_61.models.tables import (
    ReceitaInstrucao, ReceitaIngrediente,
    Receita, Ingrediente, Unidade
)
from .forms import(
    IngredienteForm,
    UnidadeForm, ReceitaInstrucaoForm,
    ReceitaIngredienteForm, ReceitaForm,
    ReceitaIngredientesInstructionsForm
)
from flask_login import login_user, logout_user, current_user, login_required
from datetime import timedelta

@app.route("/")
def index():
    receitas = Receita.query.all()
    return render_template("index.html", receitas=receitas) 

@app.route('/ingredientes')
def ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template ('ingredientes.html', titulo="Ingredientes Disponiveis", ingredientes=ingredientes)

@app.route('/novoingrediente', methods=['POST', 'GET'])
def novoingrediente():
    form = IngredienteForm()
    ingrediente = Ingrediente(name=form.name.data)
    if form.validate_on_submit():
        db.session.add(ingrediente)
        db.session.commit()
        flash('Ingrediente Criado com Sucesso')
        return redirect(url_for('ingredientes'))
    ingredientes_qs = Ingrediente.query.all()
    return render_template ('novoingrediente.html', titulo="Novo Ingrediente", form=form)

@app.route('/ingredientes/<id>', methods=['POST', 'GET'])
def change_ingrediente(id):
    ingrediente = Ingrediente.query.get_or_404(id)
    nome = ingrediente.name
    form = IngredienteForm()
    if form.validate_on_submit():
        print(form.errors)
        ingrediente.name=form.name.data
        db.session.commit()
        flash('O Ingredientefoi Atualizado', 'success')
        return redirect(url_for("ingredientes", form=form))
    elif request.method == 'GET':
        ingrediente.name = form.name
        
    return render_template('change_ingrediente.html', titulo="Altere o seu ingrediente", ingrediente=ingrediente, form=form)

@app.route('/ingredientes/delete/<id>', methods=['POST', 'GET'])
def delete_ingrediente(id):
    ingrediente = Ingrediente.query.get_or_404(id)
    db.session.delete(ingrediente)
    db.session.commit()
    flash('O Ingrediente foi deletado com Sucesso', 'success')
    return redirect(url_for("ingredientes"))

@app.route('/unidades')
def unidades():
    unidades = Unidade.query.all()
    return render_template ('unidades.html', titulo="Unidades de Medida", unidades=unidades)

@app.route('/novaunidade', methods=['POST', 'GET'])
def novaunidade():
    form = UnidadeForm()
    if form.validate_on_submit():
        unidade = Unidade(name=form.name.data)
        db.session.add(unidade)
        db.session.commit()
        flash('Unidade de Medida Criada com Sucesso')
        return redirect(url_for('unidades'))
    ingredientes_qs = Ingrediente.query.all()
    return render_template ('novaunidade.html', titulo="Nova Unidade de Medida", form=form)

@app.route('/unidades/<id>', methods=['POST', 'GET'])
def change_unidade(id):
    unidade = Unidade.query.get_or_404(id)
    nome = unidade.name
    form = UnidadeForm()
    if form.validate_on_submit():
        print(form.errors)
        unidade.name=form.name.data
        db.session.commit()
        flash('A Unidade foi Atualizada', 'success')
        return redirect(url_for("unidades", form=form))
    elif request.method == 'GET':
        unidade.name = form.name
        
    return render_template('change_unidade.html', titulo="Altere a Unidade de Medida", unidade=unidade, form=form)

@app.route('/unidades/delete/<id>', methods=['POST', 'GET'])
def delete_unidade(id):
    unidade = Unidade.query.get_or_404(id)
    db.session.delete(unidade)
    db.session.commit()
    flash('A Unidade de Medida foi deletada com Sucesso', 'success')
    return redirect(url_for("unidades"))

@app.route("/receitas", methods=["GET"])
def receitas_index():
    return redirect("/")

@app.route("/receitas/<int:id>", methods=['POST', 'GET'])
def change_receita(id):
    receita = Receita.query.get_or_404(id)
    form = ReceitaIngredientesInstructionsForm()
    # if form.validate_on_submit():
    if form.ingredientes.data and form.ingredientes.data[0]['submit'] == True:
        for indice in form.ingredientes.data:
            ingrediente = ReceitaIngrediente(
                quantity=indice['quantity'],
                receita_id=id,
                unidade_id = indice['unidade_id'].id,
                ingrediente_id = indice['ingrediente'].id
            )
            db.session.add(ingrediente)
            db.session.commit()
            return redirect(url_for('change_receita', id=receita.id))

    if form.instructions.data and form.instructions.data[0]['submit']== True:
        for indice in form.instructions.data:
            instruction = ReceitaInstrucao(
                instruction=indice['instruction'],
                receita_id=id,

            )
            db.session.add(instruction)
            db.session.commit()
            return redirect(url_for('change_receita', id=receita.id))
    receita_ingredientes_qs = ReceitaIngrediente.query.filter_by(receita_id=id)
    receita_instructions_qs = ReceitaInstrucao.query.filter_by(receita_id=id)
    return render_template('receita.html', titulo="Receita", receita=receita, form=form, receita_ingredientes_qs=receita_ingredientes_qs, receita_instructions_qs=receita_instructions_qs)

@app.route("/novareceita", methods=['POST', 'GET'])
def nova_receita():
    form = ReceitaForm()
    if form.validate_on_submit():
        receita = Receita(name=form.name.data)
        db.session.add(receita)
        db.session.commit()
        flash('ReceitaCriada com Sucesso')
        return redirect(url_for('receita', id=receita.id))
    return render_template ('novareceita.html', titulo="Nova Receita", form=form)

@app.route("/receitas/ingredientes/<int:id>/delete", methods=['POST', 'GET'])
def delete_receita_ingrediente(id):
    receita_ingrediente = ReceitaIngrediente.query.get_or_404(id)
    receita = Receita.query.get_or_404(receita_ingrediente.receita_id)
    db.session.delete(receita_ingrediente)
    db.session.commit()
    flash('Esse ingrediente foi deletado com sucesso desta receita', 'success')
    return redirect(url_for('change_receita', id=receita.id))

@app.route("/receitas/instructions/<int:id>/delete", methods=['POST', 'GET'])
def delete_receita_instrucao(id):
    receita_instruction = ReceitaInstrucao.query.get_or_404(id)
    receita = Receita.query.get_or_404(receita_instruction.receita_id)
    db.session.delete(receita_instruction)
    db.session.commit()
    flash('Essa instrução foi deletada com sucesso desta receita', 'success')
    return redirect(url_for('change_receita', id=receita.id))