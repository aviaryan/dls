# DLS

Direct Link Service


## Setting up locally

To run locally, first create the database

```sql
create user project with password 'project';
create database dls with owner=project;
```
Once database is created, use `bash runserver.sh`.

One can also use `python runserver.py`.


## Setting up on Heroku

First set up env vars for this project.

```bash
heroku config:set CONFIG=config.HerokuConfig 
heroku config:set DATABASE_URL=postgresql://localhost/dls 
```

Then update the DATABASE_URL.

```bash
heroku addons:add heroku-postgresql:dev
heroku pg:promote HEROKU_POSTGRESQL_COLOR_URL # change DATABASE_URL to heroku's database
```

Done