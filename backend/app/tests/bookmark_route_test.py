"""
Test script for bookmark candidates.
version 1.0
Author - WaleedAhmed05
"""
import unittest
from unittest.mock import patch
import app


class TestCandidateBookmarkRoutes(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    @patch('controllers.candidate_bookmark_controller.CandidateBookmarkController.bookmark_candidate')
    def test_bookmark_candidate(self, mock_bookmark_candidate):
        # Mock the CandidateBookmarkController.bookmark_candidate() method
        mock_bookmark_candidate.return_value = {'message': 'Candidate bookmarked successfully'}

        # Simulating post request.
        response = self.app.post('/api/bookmark_candidate/101', json={'candidate_id': 101})

        # if status code is 200 (OK), it means it's passed.
        self.assertEqual(response.status_code, 200)

        # Check if the response JSON matches the expected success message
        self.assertEqual(response.json, {'message': 'Candidate bookmarked successfully'})

    @patch('controllers.candidate_bookmark_controller.CandidateBookmarkController.bookmark_candidate')
    def test_bookmark_candidate_error(self, mock_bookmark_candidate):
        # Mock the CandidateBookmarkController.bookmark_candidate() method
        mock_bookmark_candidate.side_effect = Exception('Some error occurred')

        # Simulate a POST request with some JSON data (request data)
        response = self.app.post('/api/bookmark_candidate/102', json={'candidate_id': 102})

        # Check if the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response JSON contains the error message
        self.assertEqual(response.json, {'error': 'Some error occurred'})

