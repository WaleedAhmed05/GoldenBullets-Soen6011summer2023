"""
Test script for browse candidates.
version 1.0
Author - WaleedAhmed05
"""
import unittest
from unittest.mock import patch
import app

class TestAuthRoutes(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    @patch('controllers.browse_candidates_controller.BrowseCandidatesController.get_all_candidates')
    def test_get_all_candidates(self, mock_get_all_candidates):
        # Mock the BrowseCandidatesController.get_all_candidates() method
        mock_get_all_candidates.return_value = [{'name': 'Waleed'}, {'name': 'Goku'}]
        response = self.app.get('/api/browse_candidates/allcandidates')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'name': 'Waleed'}, {'name': 'Goku'}])

    @patch('controllers.browse_candidates_controller.BrowseCandidatesController.get_all_candidateskills')
    def test_get_all_skills(self, mock_get_all_candidateskills):
        # Mock the BrowseCandidatesController.get_all_candidateskills() method
        mock_get_all_candidateskills.return_value = ['Skill1', 'Skill2', 'Skill3']
        response = self.app.get('/api/browse_candidates/allcandidateskills')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, ['Skill1', 'Skill2', 'Skill3'])

    @patch('controllers.browse_candidates_controller.BrowseCandidatesController.get_all_candidates')
    def test_get_all_candidates_error(self, mock_get_all_candidates):
        # Simulate an exception in BrowseCandidatesController.get_all_candidates()
        mock_get_all_candidates.side_effect = Exception('Some error occurred')
        response = self.app.get('/api/browse_candidates/allcandidates')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'error': 'Some error occurred'})

    @patch('controllers.browse_candidates_controller.BrowseCandidatesController.get_all_candidateskills')
    def test_get_all_skills_error(self, mock_get_all_candidateskills):
        # Simulate an exception in BrowseCandidatesController.get_all_candidateskills()
        mock_get_all_candidateskills.side_effect = Exception('Another error occurred')
        response = self.app.get('/api/browse_candidates/allcandidateskills')
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'error': 'Another error occurred'})

