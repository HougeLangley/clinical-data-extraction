from ..modules import patient, medication

def get_patient_by_id(patient_id):
    return Patient.query.get(patient_id)

def get_all_patients():
    return Patient.query.all()

def add_patient(name, patient_id):
    new_patient = Patient(name=name, patient_id=patient_id)
    db.session.add(new_patient)
    db.session.commit()
    return new_patient

def get_medication_by_patient_id(patient_id):
    return Medication.query.filter_by(patient_id=patient_id).all()