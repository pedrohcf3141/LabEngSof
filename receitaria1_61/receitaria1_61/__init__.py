__version__ = '0.1.0'

from flask import Flask

app = Flask(__name__)
app.secret_key = "receitaria"

from receitaria1_61.controllers import urls
