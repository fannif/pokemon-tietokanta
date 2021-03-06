from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else: 
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///individuals.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views

from application.individuals import models
from application.individuals import views

from application.auth import models
from application.auth import views

from application.types import models
from application.types.models import Type

from application.species import models
from application.species import views
from application.species.models import SpeciesType
from application.species.models import speciestype

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "You must be logged in to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.mapper(SpeciesType, speciestype)
    db.create_all()
except:
    pass

if not Type.query.all():
    db.session.add(Type("bug"))
    db.session.add(Type("dark"))
    db.session.add(Type("dragon"))
    db.session.add(Type("electric"))
    db.session.add(Type("fairy"))
    db.session.add(Type("fighting"))
    db.session.add(Type("fire"))
    db.session.add(Type("flying"))
    db.session.add(Type("ghost"))
    db.session.add(Type("grass"))
    db.session.add(Type("ground"))
    db.session.add(Type("ice"))
    db.session.add(Type("normal"))
    db.session.add(Type("poison"))
    db.session.add(Type("psychic"))
    db.session.add(Type("rock"))
    db.session.add(Type("steel"))
    db.session.add(Type("water"))
    db.session.commit()

