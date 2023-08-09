"""
Test script for API routes.
This script is testing real API values stored in Project DB.
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





    def test_company_values(self):

        #mock_company_description="Optimizely is an American company that provides digital experience platform software as a service."
        mock_company_description = "We are a big company!"
        mock_company_id =1
        mock_company_name = "Optimizely"
        mock_company_industry = "Marketing"
        mock_company_website = "https://www.optimizely.com"
        mock_company_num_employees = 1000


        response = self.app.get('/api/jobs/1')
        data = response.get_json()

        self.assertEqual(data['company']['description'], mock_company_description)
        self.assertEqual(data['company']['id'], mock_company_id)
        self.assertEqual(data['company']['name'], mock_company_name)
        self.assertEqual(data['company']['industry'], mock_company_industry)
        self.assertEqual(data['company']['website'], mock_company_website)
        self.assertEqual(data['company']['num_employees'], mock_company_num_employees)

    def test_company_jobs(self):
        mock_job_description = "Optimizely is looking for a Scrum Master with 3+ years of experience. Please join our team 🥺"
        mock_company_id = 1
        mock_job_type="full_time"
        mock_location="Dhaka"
        mock_salary="BDT 100,000"
        mock_title="Scrum Master"

        response = self.app.get('/api/jobs/2')
        data = response.get_json()

        self.assertEqual(data['company_id'], mock_company_id)
        self.assertEqual(data['description'], mock_job_description)
        self.assertEqual(data['job_type'], mock_job_type)
        self.assertEqual(data['location'], mock_location)
        self.assertEqual(data['salary'], mock_salary)
        self.assertEqual(data['title'], mock_title)


if __name__ == '__main__':
    unittest.main()