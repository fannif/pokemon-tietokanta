from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user, login_manager
from application.individuals.models import Individual
from application.individuals.forms import IndividualForm, EditIndividualForm, SearchIndividualForm
from application.species.models import Species
from application.species.forms import SpeciesForm
from flask_paginate import Pagination, get_page_parameter

@app.route("/individuals/", methods=["GET"])
@login_required
def individuals_index():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)
    individuals = Individual.query.filter_by(account_id=current_user.id)

    i = (page-1)*10
    individuals_paginated = individuals[i:i+10]

    pagination = Pagination(page=page, total=individuals.count(), search=search, record_name='individuals', per_page = 10, css_framework='bootstrap4')

    return render_template("individuals/list.html", individuals = individuals_paginated, pagination=pagination)

@app.route("/individuals/order/<order>/", methods=["GET"])
@login_required
def individuals_order(order):
    if order == "nickname":
        individuals = Individual.query.filter_by(account_id=current_user.id).order_by(Individual.nickname)
    elif order == "level":
        individuals = Individual.query.filter_by(account_id=current_user.id).order_by(Individual.level)
    else:
        individuals = Individual.query.filter_by(account_id=current_user.id).order_by(Individual.date_caught)

    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    i = (page-1)*10
    individuals_paginated = individuals[i:i+10]

    pagination = Pagination(page=page, total=individuals.count(), search=search, record_name='individuals', per_page = 10, css_framework='bootstrap4')

    return render_template("individuals/list.html", individuals = individuals_paginated, pagination=pagination)

@app.route("/individuals/new/")
@login_required
def individuals_form():
    return render_template("individuals/new.html", form = IndividualForm())

@app.route("/individuals/remove/<individual_id>/", methods=["POST"])
@login_required
def individuals_remove(individual_id):
    i = Individual.query.filter_by(id=individual_id).first()
    if i.account_id != current_user.id:
        return login_manager.unauthorized()

    db.session.delete(i)
    db.session.commit()

    return redirect(url_for("individuals_index"))

@app.route("/individuals/<individual_id>/", methods=["POST"])
@login_required
def individuals_set_favourite(individual_id):

    i = Individual.query.get(individual_id)
    if i.account_id != current_user.id:
        return login_manager.unauthorized()

    if i.favourite:
        i.favourite = False
    else:
        i.favourite = True
    db.session().commit()

    return redirect(url_for("individuals_index"))

@app.route("/individuals/show/<individual_id>/", methods=["GET"])
@login_required
def individuals_show(individual_id):
    i = Individual.query.get(individual_id)
    if i.account_id != current_user.id:
        return login_manager.unauthorized()

    species = Species.query.get(i.species_id)

    return render_template("individuals/edit.html", individual=i, species=species, form=EditIndividualForm())

@app.route("/individuals/edit/<individual_id>/", methods=["POST"])
@login_required
def individuals_edit(individual_id):
    i = Individual.query.get(individual_id)
    if i.account_id != current_user.id:
        return login_manager.unauthorized()

    form = EditIndividualForm(request.form)

    species = Species.query.get(i.species_id)
    
    if not form.validate():
        return render_template("individuals/edit.html", form=form, individual=i, species=species)

    species = Species.query.filter_by(name=form.species.data.lower()).first()

    i.nickname = form.nickname.data
    i.level = form.level.data
    i.species_id = species.id
    
    db.session.commit()
    
    return redirect(url_for("individuals_index"))

@app.route("/individuals/searchpage/", methods=["GET"])
@login_required
def individuals_searchform():
    return render_template("individuals/search.html", form=SearchIndividualForm())

@app.route("/individuals/search/", methods=["POST", "GET"])
@login_required
def individuals_search():
    form = SearchIndividualForm(request.form)

    if not form.validate():
        return render_template("individuals/search.html", form=form)

    n = form.nickname.data
    s = form.species.data.lower()
    f = form.favourite.data

    if s:
        species = Species.query.filter_by(name=s).first()

    if n and s and f:
        individuals = Individual.query.filter_by(account_id=current_user.id, nickname=n, favourite=f, species_id=species.id)
    elif n and f:
        individuals = Individual.query.filter_by(account_id=current_user.id, nickname=n, favourite=f)
    elif s and f:
        individuals = Individual.query.filter_by(account_id=current_user.id, species_id=species.id, favourite=f)
    elif n and s:
        individuals = Individual.query.filter_by(account_id=current_user.id, nickname=n, species_id=species.id)
    elif n:
        individuals = Individual.query.filter_by(account_id=current_user.id, nickname=n)
    elif s:
        individuals = Individual.query.filter_by(account_id=current_user.id, species_id=species.id)
    elif f:
        individuals = Individual.query.filter_by(account_id=current_user.id, favourite=f)
    else:
        individuals = Individual.query.filter_by(account_id=current_user.id)

    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    i = (page-1)*10
    individuals_paginated = individuals[i:i+10]

    pagination = Pagination(page=page, total=individuals.count(), search=search, record_name='individuals', per_page = 10, css_framework='bootstrap4')

    return render_template("individuals/list.html", individuals = individuals_paginated, pagination=pagination)

@app.route("/individuals/", methods=["POST"])
@login_required
def individuals_create():
    form = IndividualForm(request.form)

    if not form.validate():
        return render_template("individuals/new.html", form = form)

    species = Species.query.filter_by(name=form.species.data.lower()).first()
    if not species:
        return render_template("species/new.html", form = SpeciesForm(), taskbar='False', error = "This species does not exist yet. Please create it.")

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
