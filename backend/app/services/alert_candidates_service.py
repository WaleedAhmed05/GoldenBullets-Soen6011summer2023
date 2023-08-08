from models.job_preferences import JobPreferences
from models.job_post import JobPost


class AlertCandidatesService:
        @staticmethod
        def alert_candidates(id):
            try:
                job_post = JobPost.query.get(id)
                jobpost_detail = JobPost.serialize(job_post)

                ftitle = jobpost_detail['title']
                flocation = jobpost_detail['location']
                fjob_type = jobpost_detail['job_type']

                matching_preferences = JobPreferences.query.filter_by(  title=ftitle,
                                                                        location=flocation,
                                                                        job_type=fjob_type)

                if matching_preferences is not None:
                    return [matching_preference.serialize() for matching_preference in matching_preferences]
                else:
                    return {'error': 'No Candidate, with matching preferences, to notify'}, 400

            except Exception as e:
                print('error', e)
                return {'error': str(e)}, 500