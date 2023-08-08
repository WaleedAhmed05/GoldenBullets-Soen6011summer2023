from services.set_jobpreference_service import SetJobPreferenceService
from flask import jsonify, request

class CandidateJobPreferencesController:
    def set_job_preference(request):
        try:
            return jsonify(SetJobPreferenceService.set_job_preference(request))
        except Exception as e:
            return {'error': str(e)}, 500