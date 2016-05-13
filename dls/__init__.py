from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG', 'config.LocalConfig'))
db = SQLAlchemy(app)


import dls.views
import dls.models
