import pytest
from models.job_post import JobPost,JobTypeEnum

@pytest.fixture
def sample_job_post():
    return JobPost(
        title='Ninja Software Engineer',
        description='We are hiring a Ninja software engineer',
        location='New York',
        salary='$100,000',
        job_type=JobTypeEnum.FULL_TIME,
        employer_id=1,
        company_id=1,
        #company='Ninja Warriors',
        #created_at=datetime.now(),
        #updated_at=datetime.now(),

    )

def test_job_post_serialize(sample_job_post):
    serialized_data = sample_job_post.serialize()
    assert isinstance(serialized_data, dict)
    assert 'id' in serialized_data
    assert 'title' in serialized_data
    assert 'description' in serialized_data
    assert 'location' in serialized_data
    assert 'salary' in serialized_data
    assert 'job_type' in serialized_data
    assert 'employer_id' in serialized_data
    assert 'company_id' in serialized_data
    assert 'company' in serialized_data
    assert 'created_at' in serialized_data
    assert 'updated_at' in serialized_data

def test_job_post_created_at_default_value(sample_job_post):
    assert sample_job_post.created_at is None #created_at is None.
    #assert isinstance(sample_job_post.created_at, datetime)