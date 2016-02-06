#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import jsonify, request
from functools import wraps
from utils import find_arduino, get_json_message, check_secret_key


def arduino_registered(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        fields = request.form.to_dict()
        if not find_arduino(fields['ip_address']):
            return get_json_message(404, "This arduino don't registered")
        if not check_secret_key(fields['ip_address'], fields['secret_key']):
            return get_json_message(403, "The key is wrong.")
        return func(*args, **kwargs)
    return decorated_function

