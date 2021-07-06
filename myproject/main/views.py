# this page is to render views and do the routing task here.
from myproject import db
from myproject.main.forms import AddBalance, Withdraw
from myproject.models import MainWindow
from flask import Blueprint, redirect, url_for, render_template

main_blueprint = Blueprint('main', __name__, template_folder='templates/main')
print(main_blueprint.template_folder)
@main_blueprint.route('/add', methods=['GET', 'POST'])
def add_balance():
    print("Inside add balance method")
    form = AddBalance()
    if form.validate_on_submit():
        print("Add Balance Validated")
        amount = form.amount.data  # get the amount field from AddBalance class of forms.py
        print("The Amount is : ", amount)

        # get the old balance
        old_bal = MainWindow.query.all()
        print(old_bal)
        if len(old_bal) == 0:
            old_bal = 0
        else:
            old_bal = MainWindow.query.all()[-1].balance
        print(old_bal)
        print("Old Balance: ",old_bal)
        curr_bal = old_bal + amount
        print("Curr Balance: ", curr_bal)
        main_obj = MainWindow(deposit=amount, balance=curr_bal)
        print("Main Obj: ",main_obj)
        db.session.add(main_obj)
        db.session.commit()
        return redirect(url_for('main.show_balance'))
    return render_template('add.html', form=form)

@main_blueprint.route('/withdraw', methods=['GET', 'POST'])
def withdraw_balance():
    withdraw_form = Withdraw()
    print("Inside Withdraw Method")
    if withdraw_form.validate_on_submit():
        print("Inside Withdraw Validate")
        amount = withdraw_form.amount.data
        print("Withdrawn Data: ", amount)
        # get the old balance and fail withdraw if withdraw>balance
        old_bal = MainWindow.query.all()
        print(old_bal)
        if len(old_bal) == 0:
            old_bal = 0
        else:
            old_bal = MainWindow.query.all()[-1].balance
        print("Old Balance: ", old_bal)
        if amount>old_bal:
            print("Withdrawl Failed as not sufficient balance")
            return render_template('failed.html')
        else:
            curr_bal = old_bal - amount
            main_obj = MainWindow(withdrawl=amount, balance=curr_bal)
            db.session.add(main_obj)
            db.session.commit()
            print("Amount Deducted ")
            return redirect(url_for('main.show_balance'))
        return redirect(url_for('main.show_balance'))
    return render_template('withdraw.html', form=withdraw_form)

@main_blueprint.route('/show')
def show_balance():
    print("Inside Show Balance Method")
    old_balance = MainWindow.query.all()
    if len(old_balance) == 0:
        curr_balance = 0
    else:
        curr_balance = old_balance[-1].balance
        print("YOur Current Balance is : ", curr_balance)
    return render_template('show_balance.html', balance=curr_balance)
