#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt import JWT

# ------------------------------------------------------------------------------
# SETUP GENERAL APPLICATION
# ------------------------------------------------------------------------------

__version__ = '1.0'
app = Flask('garnet_api')
app.config.from_object('config')
app.debug = True

# ------------------------------------------------------------------------------
# SETUP LOGGING
# ------------------------------------------------------------------------------

handler = RotatingFileHandler('garnet_api.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

# ------------------------------------------------------------------------------
# SETUP MONGO DB 
# ------------------------------------------------------------------------------

db = MongoEngine(app)

# ------------------------------------------------------------------------------
# SETUP JWT AUTHENTICATION
# ------------------------------------------------------------------------------

# Import all garnet_api controller files
from garnet_api.controllers import *
from garnet_api.security import idam

jwt = JWT(app, idam.authenticate, idam.identity)
