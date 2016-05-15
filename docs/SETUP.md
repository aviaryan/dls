# Setup instructions


## Locally

To run locally, first create the database

```sql
create user project with password 'project';
create database dls with owner=project;
```
Once database is created, create the tables.

```bash
# python manage.py db migrate # to generate migration file
python manage.py db upgrade
```

Then run the server using `bash runserver.sh`. One can also use `python runserver.py`.


## On Heroku

First set up env vars for this project.

```bash
heroku config:set CONFIG=config.HerokuConfig
heroku config:set DATABASE_URL=postgresql://localhost/dls
```
Then update the DATABASE_URL.

```bash
heroku addons:add heroku-postgresql:dev
heroku pg:promote HEROKU_POSTGRESQL_COLOR_URL # change DATABASE_URL to heroku's database
# heroku pg:reset DATABASE_URL --confirm dlus # to reset the DATABASE if needed
```
Finally sync the heroku database

```bash
heroku run migrate
```
Done
