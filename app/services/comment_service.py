from app.models.comment import Comment
from app.services.service import Service

class CommentService(Service):
    def __init__(self):
        super().__init__(Comment)

    def get_comments_by_post(self, post_id):
        """Get all comments for a specific post."""
        return self.model.query.filter_by(post_id=post_id).all()
    
    def get_comments_by_user(self, user_id):
        """Get all comments made by a specific user."""
        return self.model.query.filter_by(user_id=user_id).all()