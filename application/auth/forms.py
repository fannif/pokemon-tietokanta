from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from application.auth.models import User

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class NewAccountForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=4)])
    password = PasswordField("Password", [validators.Length(min=4)])
    password_confirm = PasswordField("Confirm password", validators=[validators.DataRequired(),validators.EqualTo('password')])

    class Meta:
       csrf = False

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Sorry, that username is already taken.")

class AccountInfoForm(FlaskForm):
    password = PasswordField("Enter new Password", [validators.Length(min=4)])
    password_confirm = PasswordField("Confirm new password", validators=[validators.DataRequired(),validators.EqualTo('password')])

    class Meta:
        csrf = False
