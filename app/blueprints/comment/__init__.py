from flask import Blueprint

comment_bp = Blueprint('comment', __name__, url_prefix='/api/comments')

from . import routes