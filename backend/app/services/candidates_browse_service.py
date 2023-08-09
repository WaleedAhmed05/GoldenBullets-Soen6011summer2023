from models.candidate import Candidate
from models.skill import Skill
from models.candidate_skills import CandidateSkill

class BrowseCandidatesService:

    @staticmethod
    def get_all_candidates():
        all_candidates = Candidate.query.all()
        return [all_candidate.serialize() for all_candidate in all_candidates]

    @staticmethod
    def get_all_candidateskills():
        skills = Skill.query.all()
        return [skill.serialize() for skill in skills]
