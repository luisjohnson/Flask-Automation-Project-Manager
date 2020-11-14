# -*- coding: utf-8 -*-
"""Customer forms."""
from flask_wtf import FlaskForm
from wtforms import  StringField
from wtforms.validators import DataRequired

from .models import Customer


class CustomerForm(FlaskForm):
    """ New Customer Form"""

    name = StringField(
        "Name", validators=[DataRequired()]
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.customer = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(CustomerForm, self).validate()
        if not initial_validation:
            return False
        customer = Customer.query.filter_by(name=self.name.data).first()
        if customer:
            self.name.errors.append("Customer already registered")
            return False
        return True
