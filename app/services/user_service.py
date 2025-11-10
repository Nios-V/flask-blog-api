from app.models.user import User
from app.services.service import Service

class UserService(Service):
    def __init__(self):
        super().__init__(User)