#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from random import randrange
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

def generate_random_ip():
    not_valid = [10,127,169,172,192]
 
    first = randrange(1,256)
    while first in not_valid:
        first = randrange(1,256)
 
    ip = ".".join([str(first),str(randrange(1,256)),
    str(randrange(1,256)),str(randrange(1,256))])
    return ip
