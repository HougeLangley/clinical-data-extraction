from flask_marshmallow import Marshmallow
from .user import User
from .patient import Patient
from .medication import Medication

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class PatientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Patient

class MedicationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Medication