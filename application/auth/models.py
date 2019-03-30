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
        stmt = text("SELECT Account.username, COUNT(Individual.id) FROM Individual"
	 	    " LEFT JOIN Account ON Individual.account_id = Account.id"
		    " GROUP BY Account.username")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"username":row[0], "amount":row[1]})

        return response
