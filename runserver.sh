export DATABASE_URL=postgresql://project:project@localhost/dls
export CONFIG=config.LocalConfig
if service --status-all | grep -e '\+.*postgresql'; then
	echo service exists
else
	sudo service postgresql restart
fi
/home/aviaryan/anaconda2/bin/python runserver.py