from application import db

class Individual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_caught = db.Column(db.DateTime, default=db.func.current_timestamp())
    nickname = db.Column(db.String(144), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    favourite = db.Column(db.Boolean, nullable=False)

    def __init__(self, nickname, level):
        self.nickname = nickname
        self.level = level
        self.favourite = False
