
README:
=========

## Pacakges
flask-security
appdirs==1.4.3
arrow==0.10.0
click==6.7
Flask==0.12
Flask-SQLAlchemy==2.2
itsdangerous==0.24
Jinja2==2.9.5
MarkupSafe==1.0
MySQL-python==1.2.5
packaging==16.8
pyparsing==2.2.0
python-dateutil==2.6.0
pytz==2016.10
six==1.10.0
SQLAlchemy==1.1.6
virtualenv==15.1.0
Werkzeug==0.12

## Commands ##

### PIP Install

pip install flask
pip install -r requirements.txt

### PIP Create requirements.txt

pip freeze --local > requirements.txt

### Create Env

virtualenv test_env

### Start Env

source test_env/bin/activate

### Start Server

python main.py

### Create Tables SQLAlchemy

from main import db
db.create.all()