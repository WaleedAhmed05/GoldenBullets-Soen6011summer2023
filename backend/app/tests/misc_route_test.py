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

    # Similar tests can be added for the test_search and test_list_all_industries methods

if __name__ == '__main__':
    unittest.main()
