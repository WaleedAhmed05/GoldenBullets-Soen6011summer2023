"""
Test script for candidate
version 1.0
Author - WaleedAhmed05
"""

import pytest
from models.candidate import Candidate
from models.candidate_skills import CandidateSkill


@pytest.fixture
def candidate_instance():
    return Candidate(
        email='john@JohnTheDon.com',
        first_name='John',
        last_name='Doe',
        work_experience={'position': 'Software Engineer', 'years': 5},
        education={'degree': 'Computer Science', 'university': 'ABC University'},
        certifications=['Python', 'Java'],
        resume_url='http://JohnTheDon.com/resume',
        linkedin_url='http://JohnTheDon.com/linkedin',
        github_url='http://JohnTheDon.com/github',
        job_applications=[],
        skills=[],
    )

# Test the serialize method
def test_candidate_serialize(candidate_instance):
    expected_result = {
        'id': None,
        'email': 'john@JohnTheDon.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'work_experience': {'position': 'Software Engineer', 'years': 5},
        'education': {'degree': 'Computer Science', 'university': 'ABC University'},
        'certifications': ['Python', 'Java'],
        'resume_url': 'http://JohnTheDon.com/resume',
        'linkedin_url': 'http://JohnTheDon.com/linkedin',
        'github_url': 'http://JohnTheDon.com/github',
        'job_applications': None,
        'skills': None,
    }

    result = candidate_instance.serialize()
    assert result == expected_result


@pytest.fixture
def sample_candidate_skill():
    return CandidateSkill(
        candidate_id=1,
        skill_id=1,
    )

#test function to test candidates skills data.
def test_candidate_skill_serialize(sample_candidate_skill):
    serialized_data = sample_candidate_skill.serialize()
    assert isinstance(serialized_data, dict)
    assert 'id' in serialized_data
    assert 'candidate_id' in serialized_data
    assert 'skill_id' in serialized_data

