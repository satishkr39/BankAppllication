# this contains all the forms items required to be rendered on our main window
# we need to have numerous classes as the number of templates to be rendered
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

# this method is for add.html page
class AddBalance(FlaskForm):
    amount = IntegerField(label="Enter the Amount to be deposited : ")
    submit = SubmitField("Deposit Amount")

# this method is for withdraw.html page
class Withdraw(FlaskForm):
    amount = IntegerField(label="Enter the Amount to be withdrawn: ")
    submit = SubmitField(label="Withdraw")


