from .database import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    patient_id = db.Column(db.String(50), unique=True, nullable=False)
    medical_records = db.relationship('MedicalRecord', backref='patient', lazy=True)