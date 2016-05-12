from dls import app, db


db.create_all()
app.run(port=7000, debug=True)
