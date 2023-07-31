"""
Test script for API routes.
version 1.0
Author - WaleedAhmed05
"""

import unittest
import app


class TestApp(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_all_jobs_route(self):
        response = self.app.get('/api/jobs/')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(data['message'], 'Hello, World!')

    def test_Job_route(self):
        response = self.app.get('/api/jobs/1')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)





    def test_job_values(self):

        mock_company_description="Optimizely is an American company that provides digital experience platform software as a service."
        mock_company_id =1
        mock_company_name = "Optimizely"
        mock_company_industry = "Software"
        mock_company_website = "https://www.optimizely.com"
        mock_company_created_at = "Mon, 24 Jul 2023 15:28:25 GMT"
        mock_company_updated_at = "Mon, 24 Jul 2023 15:28:25 GMT"
        mock_company_num_employees = 1200


        response = self.app.get('/api/jobs/1')
        data = response.get_json()

        self.assertEqual(data['company']['description'], mock_company_description)
        self.assertEqual(data['company']['id'], mock_company_id)
        self.assertEqual(data['company']['name'], mock_company_name)
        self.assertEqual(data['company']['industry'], mock_company_industry)
        self.assertEqual(data['company']['website'], mock_company_website)
        self.assertEqual(data['company']['num_employees'], mock_company_num_employees)
        self.assertEqual(data['company']['created_at'],mock_company_created_at)
        self.assertEqual(data['company']['updated_at'], mock_company_updated_at)


if __name__ == '__main__':
    unittest.main()