from flask import Blueprint, request, jsonify
from flask_apispec import use_kwargs, marshal_with
from ..models import Medication, db
from ..models.schemas import MedicationSchema
from ..services.data_service import get_medication_by_patient_id

medication_bp = Blueprint('medication', __name__)

@medication_bp.route('/medications/<int:patient_id>', methods=['GET'])
@marshal_with(MedicationSchema(many=True))
def get_medications_by_patient_id(patient_id):
    medications = get_medication_by_patient_id(patient_id)
    return medications, 200

def init_app(app):
    app.register_blueprint(medication_bp)
    app.api.register('get_medications_by_patient_id', medication_bp, '/medications/<int:patient_id>')