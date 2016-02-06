#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import jsonify, request
from functools import wraps
from utils import find_arduino, get_json_message


def arduino_registered(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        fields = request.form.to_dict()
        if not find_arduino(fields['ip_address']):
            return get_json_message(404, "This arduino don't registered")
        return func(*args, **kwargs)
    return decorated_function

