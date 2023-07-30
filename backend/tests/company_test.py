import pytest
from models.company import Company


@pytest.fixture
def sample_company():
    return Company(
        name='HeckTheWorld Company',
        description='Lets hack the digital world!',
        website='www.HackOWorld.com',
        industry='IT-CyberSecurity',
        num_employees=100,
        created_by=1,
    )

def test_company_serialize(sample_company):
    serialized_data = sample_company.serialize()
    assert isinstance(serialized_data, dict)
    assert 'id' in serialized_data
    assert 'name' in serialized_data
    assert 'description' in serialized_data
    assert 'website' in serialized_data
    assert 'industry' in serialized_data
    assert 'num_employees' in serialized_data
    assert 'created_at' in serialized_data
    assert 'updated_at' in serialized_data


#Values should not be null!
def test_company_created_at_default_value(sample_company):
    assert sample_company.name is not None
    assert sample_company.description is not None
    assert sample_company.website is not None
    assert sample_company.industry is not None
    assert sample_company.num_employees is not None
    assert sample_company.created_by is not None
    #assert isinstance(sample_company.created_at, datetime)
