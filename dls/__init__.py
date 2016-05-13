from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku
from os import environ


app = Flask(__name__)
app.config.from_object(environ['CONFIG'])
heroku = Heroku(app)
db = SQLAlchemy(app)


import dls.views
import dls.models
