from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_apispec.extension import FlaskApiSpec
from flask_restful import Api
from .modules import db
from .services import data_service as data_service
from .services import ai_service as ai_service
from .services import recommendation_service as recommendation_service
from .routes import auth_routes, patient_routes, medication_routes, ai_routes
from .utils import config as cfg

db = SQLAlchemy()
ma = Marshmallow()
api = Api()
docs = FlaskApiSpec()

def create_app():
    app = Flask(__name__)
    cfg.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    docs.init_app(app, document_options={'url': '/swagger', 'title': 'Hospital System API', 'version': '1.0.0'})

    auth_routes.init_app(app)
    patient_routes.init_app(app)
    medication_routes.init_app(app)
    ai_routes.init_app(app)

    with app.app_context():
        db.create_all()

    return app