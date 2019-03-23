from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.individuals.models import Individual
from application.individuals.forms import IndividualForm

@app.route("/individuals", methods=["GET"])
@login_required
def individuals_index():
    return render_template("individuals/list.html", individuals = Individual.query.all())

@app.route("/individuals/new/")
@login_required
def individuals_form():
    return render_template("individuals/new.html", form = IndividualForm())

@app.route("/individuals/<individual_id>/", methods=["POST"])
@login_required
def individuals_set_favourite(individual_id):

    i = Individual.query.get(individual_id)
    if i.favourite:
        i.favourite = False
    else:
        i.favourite = True
    db.session().commit()

    return redirect(url_for("individuals_index"))

@app.route("/individuals/", methods=["POST"])
@login_required
def individuals_create():
    form = IndividualForm(request.form)

    if not form.validate():
        return render_template("individuals/new.html", form = form)

    n = form.nickname.data
    l = form.level.data
    i = Individual(nickname=n, level=l)
    i.favourite = form.favourite.data
    i.account_id = current_user.id

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("individuals_index"))
