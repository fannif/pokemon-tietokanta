from application import db
from application.types.models import Type
from sqlalchemy.sql import text

speciestype = db.Table("speciestype", 
        db.metadata,
        db.Column("id", db.Integer, primary_key = True),
        db.Column("species_id", db.Integer, db.ForeignKey("species.id")),
        db.Column("type_id", db.Integer, db.ForeignKey("type.id"))
        )
db.Index("link", speciestype.c.species_id, speciestype.c.type_id, unique = True)

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(512))
    legendary = db.Column(db.Boolean, nullable=False)
    types = db.relationship("Type", secondary=speciestype, lazy="subquery", backref=db.backref("typespecies", lazy=True))


    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.legendary = False

    @staticmethod
    def get_types(s):
        stmt = text("SELECT Type.name FROM Type JOIN SpeciesType ON Type.id = SpeciesType.type_id"
                    " JOIN Species ON SpeciesType.species_id = Species.id"
                    " WHERE Species.id = :id").params(id=s.id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})

        return response


class SpeciesType(object):
    def __init__(self, species_id, type_id):
        self.species_id = species_id
        self.type_id = type_id

if __name__ ==  "__main__":
    db.mapper(SpeciesType, speciestype)
