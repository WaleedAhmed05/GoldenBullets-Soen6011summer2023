# contoler for get apply form
from services.job_apply_service import ApplyFormService
from flask import jsonify

class ApplyFormController:

    def get_apply_forms():
        try:
            apply_forms = jsonify(ApplyFormService.get_apply_forms())
            return apply_forms
        except Exception as e:
            return {'error': str(e)}, 500

    def get_apply_form(id):
        try:
            apply_form = jsonify(ApplyFormService.get_apply_form(id))
            return apply_form
        except Exception as e:
            return {'error': str(e)}, 500