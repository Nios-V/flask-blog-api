from flask import jsonify, request
from . import user_bp
from app.services.user_service import UserService

service = UserService()

@user_bp.route('/', methods=['GET'])
def get_users():
    users = service.get_all()
    return jsonify([user.to_dict() for user in users]), 200

@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = service.get_by_id(id)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    user = service.create(data)
    return jsonify(user.to_dict()), 201

@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = service.update(id, data)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({'error': 'User not found'}), 404

@ user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    success = service.delete(id)
    if success:
        return jsonify({'message': 'User deleted'}), 200
    return jsonify({'error': 'User not found'}), 404
