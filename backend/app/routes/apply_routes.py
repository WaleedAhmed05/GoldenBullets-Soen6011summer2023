from flask import Blueprint, request, jsonify
from controllers.apply_form_get_controller import ApplyFormController

apply_form_routes = Blueprint('apply_form_routes', __name__, url_prefix='/api/apply')

@apply_form_routes.route('/', methods=['GET'])
def get_apply_forms():
    try:
        return ApplyFormController.get_apply_forms()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@apply_form_routes.route('/<int:id>', methods=['GET'])
def get_apply_form(id):
    try:
        return ApplyFormController.get_apply_form(id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500



