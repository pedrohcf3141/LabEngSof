__version__ = '0.1.0'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flaskext.mysql import MySQL
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
mysql = MySQL(app)
login_manager = LoginManager(app)

from receitaria1_61.controllers import urls
from .models import tables


