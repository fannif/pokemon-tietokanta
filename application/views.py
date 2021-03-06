from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html", all_species=User.users_with_all_species(), legendaries=User.users_with_legendaries())
