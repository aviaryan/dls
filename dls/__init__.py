from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
# Session = sessionmaker(bind=db)

import dls.views
import dls.models
