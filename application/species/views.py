from application import app, db 
from application.species.models import Species 
from application.species.models import speciestype
from application.species.models import SpeciesType 
from application.species.forms import SpeciesForm 
from application.individuals.forms import IndividualForm 
from flask import render_template, request, redirect, url_for

@app.route("/species/new/")
def species_form():
    return render_template("species/new.html", form = SpeciesForm())

@app.route("/species/", methods=["POST"])
def species_create():
    form = SpeciesForm(request.form)

    if not form.validate():
        return render_template("species/new.html", form = form)

    s = Species(form.name.data.lower(), form.description.data)
    s.legendary = form.legendary.data

    type1 = form.type1.data
    type2 = form.type2.data

    db.session().add(s)
    db.session().commit()

    link(s.id, type1.id)

    if type2:
        link(s.id, type2.id)

    return render_template("individuals/new.html", form = IndividualForm())

@app.route("/link/<int:species_id>/<int:type_id>")
def link(species_id, type_id):
    link = SpeciesType(species_id, type_id)
    db.session.add(link)
    db.session.commit()

@app.route("/species/<species_id>/", methods=["GET"])
def species_info(species_id):
    species = Species.query.get(species_id)
    types = species.get_types(species)

    return render_template("species/info.html", species = species, types = types)
