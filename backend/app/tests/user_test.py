"""
Test script for candidate
version 1.0
Author - WaleedAhmed05
"""

import pytest
from models.user import User

@pytest.fixture
def user_data_valid():
    # Sample candidate data for testing
    return {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Don',
        'email': 'test@example.com',
        'type' : 'candidate'
    }

def test_serialize(user_data_valid):
    user = User(**user_data_valid)
    serialized_data = user.serialize()
    assert serialized_data == user_data_valid