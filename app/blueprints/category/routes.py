from flask import jsonify, request
from . import category_bp
from app.services.category_service import CategoryService

service = CategoryService()

@category_bp.route('/', methods=['GET'])
def get_categories():
    categories = service.get_all()
    return jsonify([category.to_dict() for category in categories]), 200

@category_bp.route('/<int:id>', methods=['GET'])
def get_category(id):
    category = service.get_by_id(id)
    if category:
        return jsonify(category.to_dict()), 200
    return jsonify({'error': 'Category not found'}), 404

@category_bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json()
    category = service.create(data)
    return jsonify(category.to_dict()), 201

@category_bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json()
    category = service.update(id, data)
    if category:
        return jsonify(category.to_dict()), 200
    return jsonify({'error': 'Category not found'}), 404

@category_bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    success = service.delete(id)
    if success:
        return jsonify({'message': 'Category deleted'}), 200
    return jsonify({'error': 'Category not found'}), 404
