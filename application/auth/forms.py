from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class NewAccountForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=4)])
    password = PasswordField("Password", [validators.Length(min=4)])

    class Meta:
       csrf = False

class AccountInfoForm(FlaskForm):
    password = PasswordField("Enter new Password", [validators.Length(min=4)])

    class Meta:
        csrf = False
