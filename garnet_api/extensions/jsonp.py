#!/usr/bin/python
# -*- coding: utf-8 -*-
from functools import wraps
from flask import request, current_app


# ------------------------------------------------------------------------------
# FUNCTION JSONPFY
# ------------------------------------------------------------------------------
def enable_jsonp(fn):
    """
    Wraps a json object into a function in order to support JSON-P cross origin
    requests without the need of enabling Cross Origin Request.
    """
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(fn(*args, **kwargs))
            content = str(callback) + '(' + data + ')'
            mime_type = 'application/javascript'
            return current_app.response_class(content, mimetype=mime_type)
        else:
            return fn(*args, **kwargs)
    return decorated_function
