from models.candidate import Candidate
from models.candidate_skills import CandidateSkill
from models.skill import Skill

class BrowseCandidatesService:

    @staticmethod
    def get_all_candidates():
        all_candidates = Candidate.query.all()
        return [all_candidate.serialize() for all_candidate in all_candidates]

    @staticmethod
    def get_all_candidateskills():
        all_candidateskills = CandidateSkill.query.all()
        return [all_candidateskill.serialize() for all_candidateskill in all_candidateskills]
