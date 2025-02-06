import unittest
from flask_testing import TestCase
from app import create_app, db
from app.models import User, Patient, Medication

class TestApp(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()
        self.db = db
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_register_user(self):
        response = self.client.post('/register', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 201)
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)

    def test_login_user(self):
        with self.app.app_context():
            user = User(username='testuser', password='testpass')
            user.set_password('testpass')
            self.db.session.add(user)
            self.db.session.commit()
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)

    def test_get_patients(self):
        with self.app.app_context():
            patient = Patient(name='TestPatient', patient_id='123')
            self.db.session.add(patient)
            self.db.session.commit()
        response = self.client.get('/patients')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'TestPatient')
        self.assertEqual(data[0]['patient_id'], '123')

    def test_get_medications(self):
        with self.app.app_context():
            medication = Medication(name='TestMedication', dosage='10mg', frequency='daily', patient_id=1)
            self.db.session.add(medication)
            self.db.session.commit()
        response = self.client.get('/medications')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'TestMedication')
        self.assertEqual(data[0]['dosage'], '10mg')
        self.assertEqual(data[0]['frequency'], 'daily')