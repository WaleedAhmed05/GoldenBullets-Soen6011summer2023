"""
Test script for testing routes for all mini features .
version 1.0
Author - WaleedAhmed05
"""
import unittest
from unittest.mock import patch
import app
from flask_jwt_extended import create_access_token
import json

class MiscRouteTests(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def get_auth_token(self):
        # Generate a mock JWT token for testing
        return create_access_token(identity="test_user")

# Tests for job search  #

    @patch('controllers.job_search.JobSearchController.filter_jobs')
    def test_filter_jobs(self, mock_filter_jobs):
        # Mock the JobSearchController.filter_jobs() method
        mock_filter_jobs.return_value = [{'title': 'Job1 - Guardian of the Repositories'},
                                         {'title': 'Job2 - Prince of Bugs'}]

        # Simulate a GET request to the /filter route with query parameters
        response = self.app.get('/api/jobs/search/filter?industry=IT&location=City')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, [{'title': 'Job1 - Guardian of the Repositories'},
                                         {'title': 'Job2 - Prince of Bugs'}])

    @patch('controllers.job_search.JobSearchController.search')
    def test_search(self, mock_search):
        # Mock the JobSearchController.search() method
        # and set the return value to a list of search results
        mock_search.return_value = [{'title': 'Job3'}, {'title': 'Job4'}]

        # Simulate a GET request to the / route with query parameters
        response = self.app.get('/api/jobs/search/?query=Python')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response JSON matches the expected list of search results
        self.assertEqual(response.json, [{'title': 'Job3'}, {'title': 'Job4'}])

    @patch('controllers.job_search.JobSearchController.list_all_industries')
    def test_list_all_industries(self, mock_list_all_industries):
        # Mock the JobSearchController.list_all_industries() method
        # and set the return value to a list of industries
        mock_list_all_industries.return_value = ['IT', 'Finance', 'Healthcare']

        # Simulate a GET request to the /industries route
        response = self.app.get('/api/jobs/search/industries')

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response JSON matches the expected list of industries
        self.assertEqual(response.json, ['IT', 'Finance', 'Healthcare'])

    @patch('controllers.job_search.JobSearchController.filter_jobs')
    def test_filter_jobs_error(self, mock_filter_jobs):
        # Mock the JobSearchController.filter_jobs() method
        # and simulate an exception when called
        mock_filter_jobs.side_effect = Exception('Filter error')

        # Simulate a GET request to the /filter route with query parameters
        response = self.app.get('/api/jobs/search/filter?industry=IT&location=City')

        # Check if the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response JSON contains the error message
        self.assertEqual(response.json, {'error': 'Filter error'})

# Tests for candidate options || invitations #

    @patch('controllers.invite_candidate_controller.InviteCandidateController.invite_candidate')
    def test_invite_candidate(self, mock_invite_candidate):
        # Mock the InviteCandidateController.invite_candidate() method
        mock_invite_candidate.return_value = {'message': 'Candidate invited successfully'}

        # Simulate a POST request with some JSON data (request data)
        response = self.app.post('/api/invite_candidate/', json={'candidate_id': 101})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Candidate invited successfully'})

    @patch('controllers.invite_candidate_controller.InviteCandidateController.invite_candidate')
    def test_invite_candidate_error(self, mock_invite_candidate):
        # Mock the InviteCandidateController.invite_candidate() method
        mock_invite_candidate.side_effect = Exception('Invitation error')

        # Simulate a POST request with some JSON data (request data)
        response = self.app.post('/api/invite_candidate/', json={'candidate_id': 123})

        # Check if the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'error': 'Invitation error'})

    @patch('controllers.candidate.CandidateController.update_profile')
    def test_update_profile(self, mock_update_profile):
        # Mock the CandidateController.update_profile() method
        mock_update_profile.return_value = {'message': 'Profile updated successfully'}

        # Simulate a PUT request with some JSON data (request data)
        # attached JWT token in header of request.
        response = self.app.put('/api/candidate/123',
                                json={'name': 'John Doe', 'skills': ['Python', 'JavaScript']},
                                headers={'Authorization': f'Bearer {self.get_auth_token()}'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Profile updated successfully'})

    @patch('controllers.candidate.CandidateController.get_profile')
    def test_get_profile(self, mock_get_profile):
        # Mock the CandidateController.get_profile() method
        mock_get_profile.return_value = {'name': 'John Doe', 'skills': ['Python', 'JavaScript']}

        # Simulate a GET request to the route
        response = self.app.get('/api/candidate/123',
                                headers={'Authorization': f'Bearer {self.get_auth_token()}'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'name': 'John Doe', 'skills': ['Python', 'JavaScript']})

    @patch('controllers.candidate.CandidateController.update_profile')
    def test_update_profile_error(self, mock_update_profile):
        # Mock the CandidateController.update_profile() method
        mock_update_profile.side_effect = Exception('Update error')

        # Simulate a PUT request with some JSON data (request data)
        response = self.app.put('/api/candidate/123',
                                json={'name': 'John Doe', 'skills': ['Python', 'JavaScript']},
                                headers={'Authorization': f'Bearer {self.get_auth_token()}'})

        # Check if the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response JSON contains the error message
        self.assertEqual(response.json, {'error': 'Update error'})

    @patch('controllers.candidate.CandidateController.get_profile')
    def test_get_profile_error(self, mock_get_profile):
        # Mock the CandidateController.get_profile() method
        mock_get_profile.side_effect = Exception('Get error')

        # Simulate a GET request to the route
        response = self.app.get('/api/candidate/123',
                                headers={'Authorization': f'Bearer {self.get_auth_token()}'})

        # Check if the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'error': 'Get error'})

# Tests for portal notifications"

    @patch('controllers.notification.NotificationController.get_notifications')
    def test_get_notifications(self, mock_get_notifications):
        # Mock the behavior of get_notifications to return a list of notifications
        mock_get_notifications.return_value = [{'message': 'Notification 1'}, {'message': 'Notification 2'}]

        # Simulate a GET request with JWT token to get notifications
        response = self.app.get('/api/notifications/',
                                headers={'Authorization': f'Bearer {self.get_auth_token}'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check the response JSON  content
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertIsInstance(response_json, list)
        self.assertEqual(len(response_json), 2)

    @patch('controllers.notification.NotificationController.set_notification_as_read')
    def test_set_notification_as_read(self, mock_set_notification_as_read):
        # Mock the behavior of set_notification_as_read to return a success message
        mock_set_notification_as_read.return_value = {'message': 'Notification marked as read'}

        # Simulate a PUT request with JWT token to set notification as read
        notification_id = 2  # Replace with a valid notification ID
        response = self.app.put(f'/api/notifications/{notification_id}',
                                headers={'Authorization': f'Bearer {self.get_auth_token}'})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check the response JSON structure
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json['message'], 'Notification marked as read')

if __name__ == '__main__':
    unittest.main()
