from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, IntegerField

class IndividualForm(FlaskForm):
    nickname = StringField("Pokemon's nickname")
    level = IntegerField("Level", [validators.NumberRange(1, 100)])
    favourite = BooleanField("Favourite")

    class Meta:
        csrf = False
