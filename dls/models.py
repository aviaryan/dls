from dls import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strId = db.Column(db.String(100), unique=True)
    dataType = db.Column(db.Integer)
    text = db.Column(db.String(10000))
