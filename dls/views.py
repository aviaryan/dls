from dls import app
from flask import url_for, redirect, request


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
        return 'Hello %s' % strId
