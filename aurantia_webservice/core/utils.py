#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import jsonify

from aurantia_webservice.models import Arduino


def find_arduino(ip):
    ip_founded = Arduino.query.filter_by(ip_address=str(ip)).first()
    if ip_founded is not None:
        return True
    return False

def check_secret_key(ip, secret_key):
    arduino = Arduino.query.filter_by(ip_address=str(ip)).first()
    if secret_key != arduino.secret_key:
        return False
    return True

def get_json_message(code, message):
    resp_data = {
        'code': str(code),
        'message' : message
        }
    resp = jsonify(resp_data)
    resp.status_code = int(code)
    return resp

