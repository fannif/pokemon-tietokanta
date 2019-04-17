from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, IntegerField, ValidationError
from application import app, db
from application.species.models import Species
import re

def validate_characters(form, field):
    if not re.match("[A-Za-z0-9]+", field.data):
        raise ValidationError('Field can only include characters A - Z and 0 - 9')

def validate_search(form, field):
    if re.match("[ ;=()]+", field.data):
        raise ValidationError('Field cannot include the following characters: ; ( ) = and space')

def validate_species(form, field):
    species = Species.query.filter_by(name=field.data.lower()).first()
    if not species:
        raise ValidationError('The new species of your pokemon does not exist yet in out database. Please add it from the taskbar first.')

class IndividualForm(FlaskForm):
    nickname = StringField("Pokemon's nickname", validators=[validators.Length(min=1), validators.Length(max=20), validate_characters])
    level = IntegerField("Level", [validators.NumberRange(1, 100)])
    favourite = BooleanField("Favourite")
    species = StringField("Pokemon's species", validators=[validators.Length(min=3), validators.Length(max=20), validate_characters])

    class Meta:
        csrf = False

class EditIndividualForm(FlaskForm):
    nickname = StringField("Pokemon's nickname", validators=[validators.Length(min=1), validators.Length(max=20), validate_characters])
    level = IntegerField("Level", [validators.NumberRange(1, 100)])
    species = StringField("Pokemon's species", validators=[validators.Length(min=3), validators.Length(max=20), validate_characters, validate_species])

    class Meta:
        csrf = False

class SearchIndividualForm(FlaskForm):
    nickname = StringField("Nickname", validators=[validate_search])
    species = StringField("Species", validators=[validate_search])
    favourite = BooleanField("Include only favourite pokemon")

    class Meta:
        csrf = False
