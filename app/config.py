from os.path import dirname, abspath, join

from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy, select
from flask_bootstrap import Bootstrap

app = Flask(__name__)
db = SQLAlchemy(app)
# api = Api(app)

#config section
SECRET_KEY = 'sshh it"s a secret'
RECAPTCHA_PUBLIC_KEY = 'hello captcha'
_cwd = dirname(abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'draft_room.db')

app.config.from_object(__name__)

Bootstrap(app)