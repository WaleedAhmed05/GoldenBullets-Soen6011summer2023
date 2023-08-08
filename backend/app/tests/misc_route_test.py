"""
Test script for testing routes for all mini features .
version 1.0
Author - WaleedAhmed05
"""
import unittest
from unittest.mock import patch
import app

class MiscRouteTests(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

# Tests for Filter Jobs Routes #

    @patch('controllers.job_search.JobSearchController.get_filtered_jobs')
    def test_get_filtered_jobs(self, mock_get_filtered_jobs):
        # Mock the JobSearchController.get_filtered_jobs() method
        mock_get_filtered_jobs.return_value = [{'title': 'Job1 - Guardian of the Repositories'},
                                               {'title': 'Job2 - Prince of Bugs'}]

        # Simulate a GET request to the route
        response = self.app.get('/api/jobs/search/filter')

        self.assertEqual(response.status_code, 200)

        # Check if the response JSON matches the expected list of filtered jobs
        self.assertEqual(response.json, [{'title': 'Job1 - Guardian of the Repositories'},
                                         {'title': 'Job2 - Prince of Bugs'}])

    @patch('controllers.job_search.JobSearchController.get_filtered_jobs')
    def test_get_filtered_jobs_error(self, mock_get_filtered_jobs):
        # Mock the JobSearchController.get_filtered_jobs() method
        mock_get_filtered_jobs.side_effect = Exception('Some error occurred')

        # Simulate a GET request to the route
        response = self.app.get('/api/jobs/search/filter')

        self.assertEqual(response.status_code, 500)

        # Check if the response JSON contains the error message
        self.assertEqual(response.json, {'error': 'Some error occurred'})

if __name__ == '__main__':
    unittest.main()
