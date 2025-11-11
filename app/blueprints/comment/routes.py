from flask import jsonify, request
from . import comment_bp
from app.services.comment_service import CommentService

service = CommentService()

@comment_bp.route('/', methods=['GET'])
def get_comments():
    comments = service.get_all()
    return jsonify([comment.to_dict() for comment in comments]), 200

@comment_bp.route('/<int:id>', methods=['GET'])
def get_comment(id):
    comment = service.get_by_id(id)
    if comment:
        return jsonify(comment.to_dict()), 200
    return jsonify({'error': 'Comment not found'}), 404

@comment_bp.route('/', methods=['POST'])
def create_comment():
    data = request.get_json()
    comment = service.create(data)
    return jsonify(comment.to_dict()), 201

@comment_bp.route('/<int:id>', methods=['PUT'])
def update_comment(id):
    data = request.get_json()
    comment = service.update(id, data)
    if comment:
        return jsonify(comment.to_dict()), 200
    return jsonify({'error': 'Comment not found'}), 404

@comment_bp.route('/<int:id>', methods=['DELETE'])
def delete_comment(id):
    success = service.delete(id)
    if success:
        return jsonify({'message': 'Comment deleted'}), 200
    return jsonify({'error': 'Comment not found'}), 404
