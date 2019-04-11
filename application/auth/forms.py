import re
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from application.auth.models import User

def validate_characters(form, field):
    if not re.match("[A-Za-z0-9]+", field.data):
        raise ValidationError('Field can only include characters A - Z and 0 - 9')

def validate_password(form, field):
    if not re.match("[A-Za-z0-9!@?#]+", field.data):
        raise ValidationError('Field can only include characters A - Z and 0 - 9 and special characters ? ! @ "#"')

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class NewAccountForm(FlaskForm):
    username = StringField("Username", validators=[validators.Length(min=4), validators.Length(max=20), validate_characters])
    password = PasswordField("Password", validators=[validators.Length(min=4), validators.Length(max=20), validate_password])
    password_confirm = PasswordField("Confirm password", validators=[validators.DataRequired(),validators.EqualTo('password')])

    class Meta:
       csrf = False

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Sorry, that username is already taken.")

class AccountInfoForm(FlaskForm):
    password = PasswordField("Enter new Password", validators=[validators.Length(min=4), validators.Length(max=20), validate_password])
    password_confirm = PasswordField("Confirm new password", validators=[validators.DataRequired(),validators.EqualTo('password')])

    class Meta:
        csrf = False
