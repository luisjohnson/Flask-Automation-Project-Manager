# -*- coding: utf-8 -*-
"""Customer forms."""
from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField, SelectField

from wtforms.validators import DataRequired

from .models import Project
# from flask_automation_management_projects.customer.models import Customer


class ProjectForm(FlaskForm):
    """ New Customer Form"""

    number = StringField(
        "Number", validators=[DataRequired()]
    )

    description = TextAreaField(
        'Description'
    )

    customer = SelectField(
        "Customer",
        validators=[DataRequired("Select a Customer")],
        choices=[]
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.project = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(ProjectForm, self).validate()
        if not initial_validation:
            return False
        project = Project.query.filter_by(number=self.number.data).first()
        if project:
            self.number.errors.append("Project already registered")
            return False
        return True
