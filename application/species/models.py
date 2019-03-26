from application import db

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(512))
    legendary = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.legendary = False
