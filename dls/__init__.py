from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ.get('CONFIG', 'config.LocalConfig'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CONSTANTS
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10 mb


import dls.views
import dls.models
import dls.filters
