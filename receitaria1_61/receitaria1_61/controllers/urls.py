from typing import Dict
from receitaria1_61 import db
from flask import (
    Flask, render_template,
    url_for, request, flash,
    redirect, session
    )
from receitaria1_61 import app
from receitaria1_61.models.tables import (
    Usuario, ReceitaInstrucao, ReceitaIngrediente,
    Receita, Ingrediente, Unidade
)
from .forms import(
    UsuarioForm, IngredienteForm,
    UnidadeForm, ReceitaInstrucaoForm
)
from flask_login import login_user, logout_user, current_user, login_required
from datetime import timedelta

# app.permanent_session_lifetime = timedelta(seconds=1200)

@app.login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route("/")
def index():
    receitas = Receita.query.all()
    return render_template("index.html", receitas=receitas) 

@app.route('/usecreate', methods=['POST', 'GET'])
def create_user():
    form = UsuarioForm()
    if form.validate_on_submit():
        user = Usuario(username=form.username.data, fullname=form.fullname.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuário Criado com Sucesso')
        return redirect(url_for('index'))
    users_qs = User.query.all()
    return render_template('create_user.html', titulo="Crie o seu Login", next=next, form=form)

@app.route('/userchange', methods=['POST', 'GET'])
def change_user():
    form = UsuarioForm()
    if form.validate_on_submit():
        print(form.errors)
        current_user.username=form.username.data
        current_user.fullname=form.fullname.data
        current_user.password=form.password.data
        db.session.commit()
        flash('Os dados de sua conta foram atualizados', 'success')
        return redirect(url_for("index", form=form))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.fullname.data = current_user.fullname
        form.password.data = current_user.password

    return render_template('change_user.html', titulo="Altere o seu Login", next=next, form=form)

@app.route('/userdelete/<user_id>', methods=['POST', 'GET'])
def delete_user(user_id):
    user = Usuario.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('Os dados de sua conta foram atualizados', 'success')
    return redirect(url_for("index"))

@app.route('/login', methods=['POST', 'GET'])
def login():
    user_form = UsuarioForm()
    # next = request.args.get('next')
    if user_form.validate_on_submit():
        user = Usuario.query.filter_by(username=user_form.username.data).first()
        if user and user.password == user_form.password.data:
            login_user(user)
            session.permanent = True
            return redirect(url_for('index'))
        else:
            flash('Tente novamente')
    return render_template('login.html', titulo="Faça o seu Login", user_form=user_form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

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




# @login_required
# @app.route('/novareceita')
# def novareceita():
#     form = ReceitaForm()
#     if form.validate_on_submit():
#         user = Usuario(username=form.username.data, fullname=form.fullname.data, password=form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Usuário Criado com Sucesso')
#         return redirect(url_for('index'))
#     users_qs = User.query.all()
#     return render_template('create_user.html', titulo="Crie o seu Login", next=next, form=form)
#     return render_template ('novareceita.html', titulo="Nova Receita")

#     form = RecipeForm()
#         ingredients_template_form = RecipeIngredientForm(prefix="ingredients-_-")
#         instructions_template_form = RecipeInstructionForm(prefix="instructions-_-")

#         return render_template(
#             "recipes/new.html",
#             form=form,
#             _ingredients_template=ingredients_template_form,
#             _instructions_template=instructions_template_form
#         )


# @app.route('/receita/<int:receita_id>')
# def receita(receita_id):
#     receita = lista_receitas[receita_id]
#     return render_template ('receita.html', titulo="Receita", receita=receita)


