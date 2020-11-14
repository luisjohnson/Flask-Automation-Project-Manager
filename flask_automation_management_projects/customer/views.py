
from flask import Blueprint, render_template, redirect, url_for
# from flask_login import login_required

from .models import Customer
from .forms import CustomerForm

blueprint = Blueprint("customer", __name__, url_prefix="/customer", static_folder="../static")


@blueprint.route("/")
def customers():
    """ List Customers. """
    data = Customer.all()
    return render_template("customers/customers.html", customers=data)


@blueprint.route("/add", methods=["GET", "POST"])
def add():
    """ Add a new Customer"""
    form = CustomerForm()
    if form.validate_on_submit():
        Customer.create(
            name=form.user.data
        )
        return redirect(url_for("customers.customers"))
    else:
        pass
    return render_template("customers/add.html", form=form)
