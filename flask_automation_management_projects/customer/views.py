
from flask import Blueprint, render_template, redirect, url_for, request, flash
# from flask_login import login_required

from .models import Customer
from .forms import CustomerForm
from flask_automation_management_projects.utils import flash_errors


blueprint = Blueprint("customer", __name__, url_prefix="/customers", static_folder="../static")


@blueprint.route("/")
def customers():
    """ List Customers. """
    data = Customer.all()
    return render_template("customers/customers.html", customers=data)


@blueprint.route("/add/", methods=["GET", "POST"])
def add():
    """ Add a new Customer"""
    form = CustomerForm(request.form)
    if form.validate_on_submit():
        Customer.create(
            name=form.name.data
        )
        return redirect(url_for("customer.customers"))
    else:
        flash_errors(form)
    return render_template("customers/add.html", form=form)
