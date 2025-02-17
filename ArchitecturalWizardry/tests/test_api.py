import unittest
from flask import json
from api import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_hubspot_field(self):
        response = self.app.post('/api/hubspot/fields', data=json.dumps({
            'field_name': 'test_field',
            'field_type': 'string'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_update_hubspot_field(self):
        response = self.app.put('/api/hubspot/fields/test_field', data=json.dumps({
            'new_field_name': 'updated_test_field'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_update_upso_cadence(self):
        response = self.app.put('/api/upso/cadences', data=json.dumps({
            'cadence_name': 'test_cadence',
            'timing': 'daily',
            'email_template': 'Test template'
        }), content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
