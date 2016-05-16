from dls import app, db, MAX_UPLOAD_SIZE
from flask import url_for, redirect, request, render_template, make_response, \
    abort, flash, Response, jsonify
from models import Data
from utils import *
import binascii


@app.route('/')
def index():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(error):
    return '404. This page does not exist', 404


@app.route('/<strId>/')
def serve(strId):
    status = getType(strId)
    return render_template('display_data.html', type=status, data=getData(strId))


def flash_to_editData(msg, strId):
    flash(msg, 'error')
    return redirect(url_for('editData', strId=strId))


@app.route('/<strId>/edit/', methods=['GET', 'POST'])
def editData(strId):
    if request.method == 'POST':
        data = Data.query.filter_by(strId=strId).first()
        if data is not None:
            if not data.is_editable():
                return flash_to_editData('This URL is locked', strId)
            data.text = request.form['text']
            data.texttime = getCurTime()
        else:
            data = Data(strId=strId, text=request.form['text'], texttime=getCurTime())
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('serve', strId=strId))
    else:
        data = Data.query.filter_by(strId=strId).first()
        if data is None:
            data = {'strId': strId}
        return render_template('edit_form.html', data=data)


@app.route('/<strId>/file', methods=['GET', 'POST'], strict_slashes=False)
def dataFile(strId):
    if request.method == 'POST':
        file = request.files['file']
        filedata = file.read()
        # if size limit exceeds
        if len(filedata) > MAX_UPLOAD_SIZE:
            return flash_to_editData('Upload size limit exceeded', strId)
        # if no file
        if len(filedata) == 0:
            return flash_to_editData('No file selected', strId)

        b64_file = binascii.b2a_base64(filedata)
        data = Data.query.filter_by(strId=strId).first()
        if data is not None:
            if not data.is_editable():
                return flash_to_editData('This URL is locked', strId)
            data.filename = file.filename
            data.fileblob = b64_file
            data.filetime = getCurTime()
            data.filesize = len(filedata)
        else:
            data = Data(strId=strId, filename=file.filename, fileblob=b64_file,
                        filetime=getCurTime(), filesize=len(filedata))
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('serve', strId=strId))
    else:
        data = Data.query.filter_by(strId=strId).first()
        if data is None or not data.filename:
            abort(404)
        response = make_response(binascii.a2b_base64(data.fileblob))
        response.headers['Content-Disposition'] = 'attachment; filename=%s' % data.filename
        return response


@app.route('/<strId>/text', strict_slashes=False)
def dataText(strId):
    data = Data.query.filter_by(strId=strId).first()
    if data is None:
        return Response(response='', status=404)
    else:
        return Response(response=data.text, status=200, content_type='text/plain; charset=utf-8')


@app.route('/<strId>.json')
def dataJSON(strId):
    data = Data.query.filter_by(strId=strId).first()
    if data is None:
        return jsonify(), 404
    else:
        json = data.as_dict()
        del json['fileblob']
        return jsonify(**json)


@app.route('/<strId>/lock', methods=['POST'])
def lock(strId):
    data = Data.query.filter_by(strId=strId).first()
    if data is None:
        abort(404)
    else:
        if strId in ['flask', 'foraman']:  # well
            flash('This URL is not lockable :p')
        else:
            data.locktime = getCurTime()
            db.session.add(data)
            db.session.commit()
        return redirect(url_for('serve', strId=strId))
