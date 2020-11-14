
from flask_automation_management_projects.database import (
    Column,
    PkModel,
    db,
    reference_col,
    relationship
)


class Project(PkModel):
    """ Project table."""

    __tablename__ = "project"
    number = Column(db.String(80), unique=True, nullable=False)
    description = Column(db.String(120))
    customer_id = reference_col("customer", nullable=True)
    customer = relationship("Customer", backref="projects")

    def __init__(self, number, **kwargs):
        """Create instance."""
        super().__init__(number=number, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Project({self.number})>"
