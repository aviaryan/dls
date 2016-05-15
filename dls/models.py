from dls import db
from datetime import datetime, timedelta


TIMELIMIT = 24 * 3600


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strId = db.Column(db.String(100), unique=True)
    text = db.Column(db.Text)
    fileblob = db.Column(db.Text)
    filename = db.Column(db.String(100))
    filesize = db.Column(db.Integer)
    filetime = db.Column(db.DateTime)
    texttime = db.Column(db.DateTime)
    locktime = db.Column(db.DateTime)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def is_locked(self):
        if self.locktime is None:
            return False
        timedelta = datetime.now() - self.locktime
        if timedelta.total_seconds() > TIMELIMIT:
            return False
        else:
            return True

    def time_remaining(self):
        if self.is_locked():
            return ((self.locktime + timedelta(seconds=TIMELIMIT)) -
                    datetime.now()).total_seconds()
        else:
            return 0

    def is_editable(self):
        return (not self.is_locked())
