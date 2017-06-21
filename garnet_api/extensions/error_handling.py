#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import jsonify


class ErrorResponse:
    def __init__(self, message, details):
        self.msg = message
        self.details = details

    def as_json(self):
        return jsonify({
            "Error": True,
            "msg": self.msg,
            "details": self.details
        })


class SuccessResponse:
    def __init__(self, result, message, details):
        self.msg = message
        self.details = details
        self.result = result

    def as_json(self):
        return jsonify({
            "result": self.result,
            "msg": self.msg,
            "details": self.details
        })