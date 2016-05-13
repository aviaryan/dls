export DATABASE_URL=postgresql://project:project@localhost/dls
export CONFIG=config.LocalConfig
sudo service postgresql restart
/home/aviaryan/anaconda2/bin/python runserver.py