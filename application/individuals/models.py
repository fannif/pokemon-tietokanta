from application import db
from sqlalchemy.sql import text

class Individual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_caught = db.Column(db.DateTime, default=db.func.current_timestamp())
    nickname = db.Column(db.String(144), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    favourite = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=False)

    def __init__(self, nickname, level):
        self.nickname = nickname
        self.level = level
        self.favourite = False

    @staticmethod
    def get_species(i):
        stmt = text("SELECT Species.name FROM Species JOIN Individual"
                    " ON Species.id = Individual.species_id"
                    " WHERE Individual.id = :id").params(id=i.id)
        s = db.engine.execute(stmt)
        species = "null"
        for row in s:
            species = row[0]

        return species
