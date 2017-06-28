from garnet_api import app
from flask import request, jsonify
from garnet_api.models.account import User
from garnet_api.models.account import UserService
from garnet_api.security.idam import find_user
from garnet_api.extensions.jsonp import enable_jsonp
from garnet_api.extensions.error_handling import ErrorResponse
from garnet_api.extensions.error_handling import SuccessResponse
from flask_jwt import jwt_required, current_identity
import uuid


# --------------------------------------------------------------------------
# GET ACCOUNT
# --------------------------------------------------------------------------
# Gets the account information associated with current session in the system
@app.route('/api/v1/account', methods=['GET'])
@jwt_required()
@enable_jsonp
def get_account():
    return current_identity.as_json()


# --------------------------------------------------------------------------
# GET: /account/<uid>
# --------------------------------------------------------------------------
@app.route('/api/v1/account/<user_id>', methods=['GET'])
@jwt_required()
@enable_jsonp
def get_account_by_id(user_id):
    identity = find_user(user_id)
    if identity:
        return identity.as_json()
    return ErrorResponse('User not found', 'The provided user_id is not valid').as_json()


# --------------------------------------------------------------------------
# PUT: /account/<uid>/password
# --------------------------------------------------------------------------
@app.route('/api/v1/account/<user_id>/password', methods=['PUT'])
@jwt_required()
@enable_jsonp
def update_account_password(user_id):
    try:
        pass_data = request.get_json()
        user_service = UserService(user_id)
        usr = user_service.get_user()
        if user_id == current_identity.id:
            if usr.update_password(pass_data['password']):
                app.logger.info('Updated password for user_id: %s', user_id)
                return SuccessResponse('Success', 'Password updated successfully', 'EMAIL_OK').as_json()
        else:
            app.logger.error('Permission violation. User not authorized to update other user\'s password. User performing operation %s', user_id)
            return ErrorResponse('Permission violation', 'This action generated a security alert').as_json()
    except:
        app.logger.error('Invalid json received for user: %s', user_id)
        return ErrorResponse('Could not update password', 'Invalid password provided').as_json()


# --------------------------------------------------------------------------
# PUT: /account/<uid>/email
# --------------------------------------------------------------------------
@app.route('/api/v1/account/<user_id>/email', methods=['PUT'])
@jwt_required()
@enable_jsonp
def update_account_email(user_id):
    try:
        email_data = request.get_json()
        user_service = UserService(user_id)
        user = user_service.get_user()
        if user.update_email(email_data['email']):
            app.logger.info('Updated email for user_id: %s', user_id)
            return SuccessResponse('Success', 'Email updated successfully', 'EMAIL_OK').as_json()
    except:
        app.logger.error('Invalid json received for user: %s', user_id)
        return ErrorResponse('Could not update email', 'Invalid email provided').as_json()


# --------------------------------------------------------------------------
# POST: /account
# --------------------------------------------------------------------------
# Registers a new user in the system using garnet_api Identity Sub-System
@app.route('/api/v1/account', methods=['POST'])
@enable_jsonp
def post_account():
    user_data = request.get_json()
    if user_data:
        user = User(
            user_id=str(uuid.uuid4()),
            name=user_data['name'],
            last_name=user_data['last_name'],
            email=user_data['email'],
            username=user_data['username'],
            password=None
            )
        user.update_password(user_data['password'])
        user.save(validate=True)
        app.logger.info('User %s was created', user.user_id)
        return SuccessResponse(user.user_id, 'User created successfully', 'n/a').as_json()
    return ErrorResponse('Error processing request', 'The provided data is not valid').as_json()