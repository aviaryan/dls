from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.LocalConfig')
db = SQLAlchemy(app)

import dls.views
import dls.models
