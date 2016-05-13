from dls import app, db, heroku


db.create_all()
app.run()
