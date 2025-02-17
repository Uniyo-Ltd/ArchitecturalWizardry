import unittest
from models import HubSpotField, UpsoEmailCadence, Session

class TestModels(unittest.TestCase):

    def test_hubspot_field(self):
        with Session() as session:
            new_field = HubSpotField(field_name='test_field', field_type='string')
            session.add(new_field)
            session.commit()
            queried_field = session.query(HubSpotField).filter_by(field_name='test_field').first()
            self.assertIsNotNone(queried_field)
            self.assertEqual(queried_field.field_name, 'test_field')

    def test_upso_email_cadence(self):
        from datetime import timedelta
        with Session() as session:
            new_cadence = UpsoEmailCadence(cadence_name='test_cadence', timing=timedelta(days=1), email_template='test_template')
            session.add(new_cadence)
            session.commit()
            queried_cadence = session.query(UpsoEmailCadence).filter_by(cadence_name='test_cadence').first()
            self.assertIsNotNone(queried_cadence)
            self.assertEqual(queried_cadence.cadence_name, 'test_cadence')

if __name__ == '__main__':
    unittest.main()
