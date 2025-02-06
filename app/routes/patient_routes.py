from flask import Blueprint, request, jsonify
from flask_apispec import use_kwargs, marshal_with
from ..models import Patient, db
from ..models.schemas import PatientSchema
from ..services.data_service import get_patient_by_id, get_all_patients, add_patient

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/patients', methods=['GET'])
@marshal_with(PatientSchema(many=True))
def get_patients():
    return get_all_patients(), 200

@patient_bp.route('/patients/<int:patient_id>', methods=['GET'])
@marshal_with(PatientSchema())
def get_patient(patient_id):
    patient = get_patient_by_id(patient_id)
    if not patient:
        return jsonify({"message": "Patient not found"}), 404
    return patient, 200

@patient_bp.route('/patients', methods=['POST'])
@use_kwargs(PatientSchema(exclude=('id',)))
@marshal_with(PatientSchema())
def create_patient(name, patient_id):
    if not name or not patient_id:
        return jsonify({"message": "Name and patient_id are required"}), 400

    new_patient = add_patient(name, patient_id)
    return new_patient, 201

def init_app(app):
    app.register_blueprint(patient_bp)
    app.api.register('get_patients', patient_bp, '/patients')
    app.api.register('get_patient', patient_bp, '/patients/<int:patient_id>')
    app.api.register('create_patient', patient_bp, '/patients')