from dls import app, db
from flask import url_for, redirect, request, render_template
from models import Data
from utils import *


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'This service was created by Avi Aryan as an attempt to learn Flask'


@app.route('/<strId>/', methods=['POST', 'GET'])
def serve(strId):
    if request.method == 'POST':
        servType = request.form['type']
        if servType == 'file':
            pass
        elif servType == 'text':
            pass
        return redirect(url_for('serve', strId=strId))
    else:
        status = getType(strId)
        return render_template('display_data.html', type=status, text=getText(strId))


@app.route('/<strId>/text/', methods=['GET', 'POST'])
def addText(strId):
    if request.method == 'POST':
        data = Data.query.filter_by(strId=strId).first()
        if data is not None:
            data.text = request.form['text']
        else:
            data = Data(strId=strId, text=request.form['text'], dataType=1)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('serve', strId=strId))
    else:
        data = Data.query.filter_by(strId=strId).first()
        if data is None:
            data = {}
        return render_template('form_text.html', data=data)
