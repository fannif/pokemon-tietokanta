from application import db
from sqlalchemy.sql import text

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    individuals = db.relationship("Individual", backref='account', lazy=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


    @staticmethod
    def find_number_of_individuals():
        stmt = text("SELECT Account.username, COUNT(Individual.id) FROM Account"
	 	    " LEFT JOIN Individual ON Individual.account_id = Account.id"
		    " GROUP BY Account.username")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"username":row[0], "amount":row[1]})

        return response


    @staticmethod
    def users_with_all_species():
        stmt = text("SELECT Account.username, COUNT(Species.name) FROM Account"
                    " LEFT JOIN Individual ON Account.id = Individual.account_id"
                    " JOIN Species ON Individual.species_id = Species.id"
                    " GROUP BY Account.username HAVING COUNT(Species.name)"
                    " = (SELECT COUNT(*) FROM Species)")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"username":row[0]})

        return response

    @staticmethod
    def users_with_legendaries():
        stmt = text("SELECT Account.id, Account.username, COUNT(Species.id) AS amount"
                    " FROM Account LEFT JOIN Individual ON Account.id = Individual.account_id"
                    " JOIN Species ON Individual.species_id = Species.id WHERE"
                    " Species.legendary = '1' GROUP BY Account.id HAVING COUNT(Species.id) > 0"
                    " ORDER BY COUNT(Species.id) DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"username":row[1], "amount":row[2]})

        return response
