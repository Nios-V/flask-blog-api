from app.models.category import Category
from app.services.service import Service

class CategoryService(Service):
    def __init__(self):
        super().__init__(Category)