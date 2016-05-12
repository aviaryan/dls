from dls import app


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/about/')
def about():
    return 'This service was created by Avi Aryan as an attempt to learn Flask'
