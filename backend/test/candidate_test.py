"""
Test script for candidate
version 1.0
Author - WaleedAhmed05
"""

import pytest
from models.candidate import Candidate
from models.candidate_skills import CandidateSkill


@pytest.fixture
def candidate_data_valid():
    # Sample candidate data for testing
    return {
        'id': 1,
        'email': 'test@example.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'work_experience': {'company': 'XYZ Corp'},
        'education': {'degree': 'Bachelor of Science'},
        'certifications': {'certificate': 'Python Certified'},
        'resume_url': 'http://example.com/resume.pdf',
        'linkedin_url': 'http://linkedin.com/in/johndoe',
        'github_url': 'http://github.com/johndoe',
    }


def candidate_data_Invalid():
    # Sample candidate data for testing
    # Some of the data is intentionally missing here.
    return {
        'id': 1,
        'email': 'test@example.com',
        'first_name': 'John',
        'work_experience': {'company': 'XYZ Corp'},
        'education': {'degree': 'Bachelor of Science'},
        'certifications': {'certificate': 'Python Certified'},
        'github_url': 'http://github.com/johndoe',
    }

@pytest.fixture
def sample_candidate_skill():
    return CandidateSkill(
        candidate_id=1,
        skill_id=1,
    )



#if data is valid.
def test_serialize(candidate_data_valid):
    candidate = Candidate(**candidate_data_valid)
    serialized_data = candidate.serialize()
    assert serialized_data == candidate_data_valid

#if data is InValid
# def test_serialize_inValid(candidate_data_Invalid):
#     candidate = Candidate(**candidate_data_Invalid)
#     serialized_data = candidate.serialize()
#     assert serialized_data != candidate_data_Invalid


#test function to test candidates skills data.
def test_candidate_skill_serialize(sample_candidate_skill):
    serialized_data = sample_candidate_skill.serialize()
    assert isinstance(serialized_data, dict)
    assert 'id' in serialized_data
    assert 'candidate_id' in serialized_data
    assert 'skill_id' in serialized_data

