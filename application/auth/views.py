from flask import render_template, redirect, request, url_for 
from flask_login import login_user, logout_user, login_required, current_user

from flask_bcrypt import Bcrypt

from flask_paginate import Pagination, get_page_parameter

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, NewAccountForm, AccountInfoForm

bcrypt = Bcrypt(app)

@app.route("/auth/new/")
def auth_form():
    return render_template("auth/new.html", form = NewAccountForm())

@app.route("/auth/", methods=["POST"])
def auth_create():
    form = NewAccountForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

    a = User(form.username.data, password_hash)

    db.session().add(a)
    db.session().commit()

    return redirect(url_for("auth_login"))

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    if not bcrypt.check_password_hash(user.password, form.password.data):
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/info")
@login_required
def auth_info():
    return render_template("auth/info.html", form = AccountInfoForm())

@app.route("/auth/delete/<user_id>/", methods=["POST"])
@login_required
def auth_delete(user_id):
    u = current_user
    db.session.delete(u)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/auth/index")
@login_required
def auth_index():
    search = False
    q = request.args.get('q')
    if q:
        search = True
    page = request.args.get(get_page_parameter(), type=int, default=1)

    users_individuals = User.find_number_of_individuals()

    i = (page-1)*10
    users_paginated = users_individuals[i:i+10]

    pagination = Pagination(page=page, total=len(users_individuals), search=search, record_name='users', per_page = 10, css_framework='bootstrap4')

    return render_template("auth/list.html", users_individuals=users_paginated, pagination=pagination)

@app.route("/auth/edit/password", methods=["POST"])
@login_required
def auth_change_password():
    form = AccountInfoForm(request.form)

    if not form.validate():
        return render_template("auth/info.html", form = form)

    u = current_user
    password_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    u.password = password_hash

    db.session().commit()

    return redirect(url_for("index"))
