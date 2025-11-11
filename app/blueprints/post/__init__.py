from flask import Blueprint

post_bp = Blueprint('post', __name__, url_prefix='/api/posts')

from . import routes