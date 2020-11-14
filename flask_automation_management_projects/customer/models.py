
from flask_automation_management_projects.database import Column, PkModel, db, reference_col, relationship


class Customer(PkModel):
    """ Customer table."""

    __tablename__ = "customer"
    name = Column(db.String(80), unique=True, nullable=False)

    def __init__(self, name, **kwargs):
        """Create instance."""
        super().__init__(name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Customer({self.name})>"
