# api service for apply form
from models.apply import Apply_form
class ApplyFormService:
    @staticmethod
    def get_apply_forms():
        apply_forms = Apply_form.query.all()
        return [apply_form.serialize() for apply_form in apply_forms]
    @staticmethod
    def get_apply_form(id):
        return Apply_form.query.get(id).serialize()
