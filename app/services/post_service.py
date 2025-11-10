from app.models.post import Post
from app.services.service import Service

class PostService(Service):
    def __init__(self):
        super().__init__(Post)