from flask_wtf  import  FlaskForm
from wtforms  import (
    StringField, PasswordField,
    TextAreaField, SubmitField,
    IntegerField, SelectField, 
    FieldList, FormField,
    Form, HiddenField, FloatField
)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import(
    InputRequired, Length,
    AnyOf, DataRequired, NumberRange
)
from receitaria1_61.models.tables import (
    ReceitaInstrucao, ReceitaIngrediente,
    Receita, Ingrediente, Unidade
)

# class UsuarioForm(FlaskForm):
#     username = StringField(
#         'Username',
#         validators=[
#             DataRequired(message='Um username é exigido'),
#             Length(min=1, max=20, message= 'Máximo de 20 caracteres.')
#             ]
#         )

#     fullname = StringField(
#         'Fullname',
#         validators=[
#             DataRequired(message='Um nome completo é exigido'),
#             Length(min=1, max=20, message= 'Máximo de 20 caracteres.')
#             ]
#         )

#     password = PasswordField(
#         'Password',
#         validators=[
#             DataRequired(message='Uma senha é exigida'),
#             Length(min=1, max=20, message= 'Máximo de 20 caracteres.')
#             ]
#         )
#     submit = SubmitField('Salvar')


class IngredienteForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            DataRequired(message='Um nome é exigido'),
            Length(min=1, max=20, message= 'Máximo de 20 caracteres.')
            ]
        )
    submit = SubmitField('Salvar')


class UnidadeForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            DataRequired(message='Um nome é exigido'),
            Length(min=1, max=20, message= 'Máximo de 20 caracteres.')
            ]
        )
    submit = SubmitField('Salvar')

class ReceitaInstrucaoForm(FlaskForm):

    instruction = StringField(
        'Instruction',
        validators=[
            DataRequired(message='Uma Instrução é exigida'),
            Length(min=1, max=20, message= 'Máximo de 20 caracteres.')
            ]
        )
    submit = SubmitField('Salvar')

class ReceitaIngredienteForm(FlaskForm):
    quantity = IntegerField("Qtde", validators=[InputRequired("é obrigatório")])

    unidade_id = QuerySelectField(
        "Unidade",
        query_factory=Unidade.query.all,
        get_pk=lambda u: u.id,
        get_label=lambda u: u.name
    )

    ingrediente = QuerySelectField(
        "Ingrediente",
        query_factory=Ingrediente.query.all,
        get_pk=lambda u: u.id,
        get_label=lambda u: u.name
    )
    submit = SubmitField('Adicinar')

class ReceitaIngredientesInstructionsForm(FlaskForm):
    ingredientes = FieldList(FormField(ReceitaIngredienteForm), min_entries=1)
    instructions = FieldList(FormField(ReceitaInstrucaoForm), min_entries=1)
    submit = SubmitField('Adicinar')

class ReceitaForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            DataRequired(message='Um nome é exigido Caralho'),
            Length(min=1, max=20, message= 'Máximo de 20 caracteres.')
            ]
        )


    submit = SubmitField('Escolha um nome')