from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.individuals.models import Individual
from application.individuals.forms import IndividualForm
from application.species.models import Species
from application.species.forms import SpeciesForm

@app.route("/individuals", methods=["GET"])
@login_required
def individuals_index():
    return render_template("individuals/list.html", individuals = Individual.query.filter_by(account_id = current_user.id))

@app.route("/individuals/new/")
@login_required
def individuals_form():
    return render_template("individuals/new.html", form = IndividualForm())

@app.route("/individuals/remove/<individual_id>/", methods=["POST"])
@login_required
def individuals_remove(individual_id):
    i = Individual.query.filter_by(id=individual_id).first()
    db.session.delete(i)
    db.session.commit()

    return redirect(url_for("individuals_index"))

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

#@app.route("individuals/edit/<individual_id>/", methods=["POST"])
#@login_required
#def individuals_edit(individual_id):
    #########

@app.route("/individuals/", methods=["POST"])
@login_required
def individuals_create():
    form = IndividualForm(request.form)

    if not form.validate():
        return render_template("individuals/new.html", form = form)

    species = Species.query.filter_by(name=form.species.data.lower()).first()
    if not species:
        return render_template("species/new.html", form = SpeciesForm(), error = "This species does not exist yet. Please create it.")

    n = form.nickname.data
    l = form.level.data
    i = Individual(nickname=n, level=l)
    i.favourite = form.favourite.data
    i.account_id = current_user.id
    i.species_id = species.id

    i.species_id = species.id

    db.session().add(i)
    db.session().commit()

    return redirect(url_for("individuals_index"))
