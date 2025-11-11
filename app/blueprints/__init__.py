from .user import user_bp
from .post import post_bp
from .category import category_bp
from .comment import comment_bp
from .auth import auth_bp

def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(comment_bp)
    app.register_blueprint(auth_bp)