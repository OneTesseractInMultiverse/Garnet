#!/usr/bin/python
# -*- coding: utf-8 -*-
from garnet_api import app
from garnet_api.models.account import User
from mongoengine import *

# ------------------------------------------------------------------------------
# IDENTITY AND ACCESS MANAGEMENT MODULE
# ------------------------------------------------------------------------------
# This section provides identity and access management functions and class
# definitions.


# ------------------------------------------------------------------------------
# FUNCTION AUTHENTICATE
# ------------------------------------------------------------------------------
# Checks given credential in order to authenticate or deny authentication to the
# API.
def authenticate(username, password):
    try:
        user = User.objects.get(username=username)
        if user and user.authenticate(password=password):
            app.logger.warning('Authenticated user with correct credentials user: '+username)
            return user.get_identity()
        else:
            app.logger.warning('User: attempted to login using invalid credentials. ' + username)
    except DoesNotExist:
        app.logger.warning('A logging attempt of non-existing user: occurred. ' + username)
    except MultipleObjectsReturned:
        app.logger.error('The username has more than 1 match in database. Urgent revision required. '+username)
    return None


# ------------------------------------------------------------------------------
# FUNCTION IDENTITY
# ------------------------------------------------------------------------------
# Gets the User associated with a given identity
def identity(payload):
    try:
        user_id = payload['identity']
        user = User.objects.get(user_id=user_id)
        return user.get_identity()
    except DoesNotExist:
        app.logger.warning('A retrieval attempt of non-existing user occurred: ' + user_id)
    except MultipleObjectsReturned:
        app.logger.error('The username has more than 1 match in database. Urgent revision required. '+user_id)
    return None


# ------------------------------------------------------------------------------
# FIND USER
# ------------------------------------------------------------------------------
def find_user(user_id):
    try:
        user = User.objects.get(user_id=user_id)
        return user.get_identity()
    except DoesNotExist:
        app.logger.warning('A retrieval attempt of non-existing user occurred: ' + user_id)
    except MultipleObjectsReturned:
        app.logger.error('The username has more than 1 match in database. Urgent revision required. ' + user_id)
    return None