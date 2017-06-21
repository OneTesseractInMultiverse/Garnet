#!/usr/bin/python
# -*- coding: utf-8 -*-
# run.py
import os
from garnet_api import app

"""
    Garnet API is a boilerplate application that allows you to create Python + Flask API
    applications based on a Model-View-Controller (MVC) pattern. It supports out of the
    box interaction with Mongo DB Document Database, JWT Token Generation and Authentication,
    basic and extensible identity model 
"""

__author__ = "Pedro Guzman (pedro@subvertic.com)"
__version__ = "1.0"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run('127.0.0.1', port)
