from flask import Blueprint, request, jsonify
from flask_apispec import use_kwargs, marshal_with
from ..models import User, db
from ..models.schemas import UserSchema
from flask_bcrypt import Bcrypt

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth_bp.route('/register', methods=['POST'])
@use_kwargs(UserSchema(exclude=('id', 'password_hash')))
@marshal_with(UserSchema())
def register(username, password):
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user, 201

@auth_bp.route('/login', methods=['POST'])
@use_kwargs({'username': fields.String(required=True), 'password': fields.String(required=True)})
def login(username, password):
    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful", "user_id": user.id}), 200

def init_app(app):
    app.register_blueprint(auth_bp)
    app.api.register('register', auth_bp, '/register')
    app.api.register('login', auth_bp, '/login')