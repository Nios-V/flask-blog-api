from app.models.user import User
from app.services.service import Service

class UserService(Service):
    def __init__(self):
        super().__init__(User)

    def get_by_email(self, email):
        """Get a user by email."""
        return self.model.query.filter_by(email=email).first()
    
    def get_by_username(self, username):
        """Get a user by username."""
        return self.model.query.filter_by(username=username).first()
    
    def before_create(self, data):
        """Validate unique data before creating a user."""
        if self.get_by_id(data.get('id')):
            raise ValueError("User ID already exists.")

        if self.get_by_email(data.get('email')):
            raise ValueError("Email already exists.")
        
        if self.get_by_username(data.get('username')):
            raise ValueError("Username already exists.")
        
        return data