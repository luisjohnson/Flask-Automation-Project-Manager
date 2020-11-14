
from flask import Blueprint, render_template, redirect, url_for, request, flash
# from flask_login import login_required

from .models import Project
from .forms import ProjectForm
from flask_automation_management_projects.utils import flash_errors
from flask_automation_management_projects.customer.models import Customer

blueprint = Blueprint("project", __name__, url_prefix="/projects", static_folder="../static")


@blueprint.route("/")
def projects():
    """ List Projects. """
    data = Customer.all()
    return render_template("projects/projects.html", customers=data)


@blueprint.route("/add", methods=["GET", "POST"])
def add():
    """ Add a new Project"""
    form = ProjectForm(request.form)
    form.customer.choices = [(customer.id, customer.name) for customer in Customer.all()]
    if form.validate_on_submit():
        Project.create(
            number=form.number.data,
            description=form.description.data,
            customer_id=form.customer.data
        )
        flash("Project {} created.".format(form.number.data))
        return redirect(url_for("project.projects"))
    else:
        flash_errors(form)
    return render_template("projects/add.html", form=form)
