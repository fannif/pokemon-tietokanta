import re
from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from application.types.models import Type

def validate_characters(form, field):
    if not re.match("[A-Za-z0-9]+", field.data):
        raise ValidationError('Field can only include characters A - Z and 0 - 9')

def validate_description(form, field):
    if not re.match("[A-Za-z0-9\.!?,]+", field.data):
        raise ValidationError('Field can only include characters A - Z and 0 - 9 and . , ! ?')

class SpeciesForm(FlaskForm):
    name = StringField("Pokemon species name", validators=[validators.Length(min=3), validators.Length(max=20), validate_characters])
    description = StringField("Describe this species", validators=[validators.Length(min=5), validators.Length(max=500), validate_description])
    legendary = BooleanField("Is it a legendary pokemon?")

    type1 = QuerySelectField(query_factory=lambda: Type.query.all(), get_label='name')
    type2 = QuerySelectField(query_factory=lambda: Type.query.all(), get_label='name', allow_blank=True, blank_text='none')

    class Meta:
        csrf = False
