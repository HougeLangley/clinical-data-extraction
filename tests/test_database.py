from app.models import db, User, Patient
import unittest

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_creation(self):
        user = User(username='testuser', password='testpass')
        db.session.add(user)
        db.session.commit()
        retrieved_user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(retrieved_user)

    def test_patient_creation(self):
        patient = Patient(name='testpatient', patient_id='123')
        db.session.add(patient)
        db.session.commit()
        retrieved_patient = Patient.query.filter_by(patient_id='123').first()
        self.assertIsNotNone(retrieved_patient)