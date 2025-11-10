from app.models.user import User
from app.services.service import Service

class UserService(Service):
    def __init__(self):
        super().__init__(User)

    def get_by_email(self, email):
        """Get a user by email."""
        return self.model.query.filter_by(email=email).first()