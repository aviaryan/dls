from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
import os


app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG', 'config.LocalConfig'))
heroku = Heroku(app)
db = SQLAlchemy(app)


import dls.views
import dls.models
