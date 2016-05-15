from dls import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strId = db.Column(db.String(100), unique=True)
    text = db.Column(db.Text)
    fileblob = db.Column(db.Text)
    filename = db.Column(db.String(100))
    filesize = db.Column(db.Integer)
    filetime = db.Column(db.DateTime)
    texttime = db.Column(db.DateTime)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
