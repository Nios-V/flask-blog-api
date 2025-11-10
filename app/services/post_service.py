from app.models.post import Post
from app.services.service import Service

class PostService(Service):
    def __init__(self):
        super().__init__(Post)

    def get_by_title(self, title):
        """Get a post by title."""
        return self.model.query.filter_by(title=title).first()
    
    def get_posts_by_category(self, category_id):
        """Get all posts in a specific category."""
        return self.model.query.filter_by(category_id=category_id).all()
    
    def get_posts_by_author(self, author_id):
        """Get all posts by a specific author."""
        return self.model.query.filter_by(user_id=author_id).all()