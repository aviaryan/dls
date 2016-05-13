from dls import app, db
from flask import url_for, redirect, request, render_template, make_response, abort
from models import Data
from utils import *
import binascii


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'This service was created by Avi Aryan as an attempt to learn Flask'


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist'


@app.route('/<strId>/')
def serve(strId):
    status = getType(strId)
    return render_template('display_data.html', type=status, data=getData(strId))


@app.route('/<strId>/edit/', methods=['GET', 'POST'])
def editData(strId):
    if request.method == 'POST':
        data = Data.query.filter_by(strId=strId).first()
        if data is not None:
            data.text = request.form['text']
        else:
            data = Data(strId=strId, text=request.form['text'])
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('serve', strId=strId))
    else:
        data = Data.query.filter_by(strId=strId).first()
        if data is None:
            data = {'strId': strId}
        return render_template('edit_form.html', data=data)


@app.route('/<strId>/file/', methods=['GET', 'POST'])
def dataFile(strId):
    if request.method == 'POST':
        file = request.files['file']
        b64_file = binascii.b2a_base64(file.read())
        data = Data.query.filter_by(strId=strId).first()
        if data is not None:
            data.filename = file.filename
            data.fileblob = b64_file
        else:
            data = Data(strId=strId, filename=file.filename, fileblob=b64_file)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('serve', strId=strId))
    else:
        data = Data.query.filter_by(strId=strId).first()
        if data is None or data.filename == '':
            abort(404)
        response = make_response(binascii.a2b_base64(data.fileblob))
        response.headers['Content-Disposition'] = 'attachment; filename=%s' % data.filename
        return response
