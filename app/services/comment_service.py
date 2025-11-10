from app.models.comment import Comment
from app.services.service import Service

class CommentService(Service):
    def __init__(self):
        super().__init__(Comment)