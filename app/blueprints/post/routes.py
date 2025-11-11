from flask import jsonify, request
from . import post_bp
from app.services.post_service import PostService

service = PostService()

@post_bp.route('/', methods=['GET'])
def get_posts():
    posts = service.get_all()
    return jsonify([post.to_dict() for post in posts]), 200

@post_bp.route('/<int:id>', methods=['GET'])
def get_post(id):
    post = service.get_by_id(id)
    if post:
        return jsonify(post.to_dict()), 200
    return jsonify({'error': 'Post not found'}), 404

@post_bp.route('/', methods=['POST'])
def create_post():
    data = request.get_json()
    post = service.create(data)
    return jsonify(post.to_dict()), 201

@post_bp.route('/<int:id>', methods=['PUT'])
def update_post(id):
    data = request.get_json()
    post = service.update(id, data)
    if post:
        return jsonify(post.to_dict()), 200
    return jsonify({'error': 'Post not found'}), 404

@post_bp.route('/<int:id>', methods=['DELETE'])
def delete_post(id):
    success = service.delete(id)
    if success:
        return jsonify({'message': 'Post deleted'}), 200
    return jsonify({'error': 'Post not found'}), 404