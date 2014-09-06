#Lastfm

An application for finding music events near you.

## To Install Locally
Clone lastfm and navigate to project root.

Create virtual environment and install requirements:
```sh
mkvirtualenv lastfm
pip install -r requirements.txt
```

Note: if an error is thrown when installing the requirements, export CFLAGS and try again:
```sh
export CFLAGS=-Qunused-arguments && export CPPFLAGS=-Qunused-arguments
pip install -r requirements.txt
```

Create database:
```sh
createdb lastfm
```

Sync database and Django models:
```sh
python manage.py syncdb
```

## To run Locally (from within project root directory)
```sh
workon lastfm
python manage.py runserver
```