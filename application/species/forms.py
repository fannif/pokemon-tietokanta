from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from application.types.models import Type

class SpeciesForm(FlaskForm):
    name = StringField("Pokemon species name")
    description = StringField("Describe this species")
    legendary = BooleanField("Is it a legendary pokemon?")

    type1 = QuerySelectField(query_factory=lambda: Type.query.all(), get_label='name')
    type2 = QuerySelectField(query_factory=lambda: Type.query.all(), get_label='name', allow_blank=True, blank_text='none')

    class Meta:
        csrf = False
