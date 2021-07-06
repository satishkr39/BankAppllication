# Setting our models(tables) for our application
from myproject import db

class MainWindow(db.Model):
    __tablename__ = 'maintable'
    id = db.Column(db.Integer, primary_key = True)
    deposit = db.Column(db.Integer)
    withdrawl = db.Column(db.Integer)
    balance = db.Column(db.Integer)

    def __init__(self, balance, withdrawl=0, deposit = 0):
        self.deposit = deposit
        self.balance = balance
        self.withdrawl = withdrawl

    def __repr__(self):
        return f"The Transaction is made for amount {self.deposit} and Balance is {self.balance}"