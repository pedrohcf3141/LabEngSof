from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from receitaria1_61 import app, manager


db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)