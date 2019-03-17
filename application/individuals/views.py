from application import app, db
from flask import redirect, render_template, request, url_for
from application.individuals.models import Individual

@app.route("/individuals", methods=["GET"])
def individuals_index():
    return render_template("individuals/list.html", individuals = Individual.query.all())

@app.route("/individuals/new/")
def individuals_form():
    return render_template("individuals/new.html")

@app.route("/individuals/<individual_id>/", methods=["POST"])
def individuals_set_favourite(individual_id):

    i = Individual.query.get(individual_id)
    if i.favourite:
        i.favourite = False
    else:
        i.favourite = True
    db.session().commit()

    return redirect(url_for("individuals_index"))

@app.route("/individuals/", methods=["POST"])
def individuals_create():
    n = request.form.get("nickname")
    l = request.form.get("level")
    i = Individual(nickname=n, level=l)

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("individuals_index"))
