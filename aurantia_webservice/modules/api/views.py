#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Blueprint, jsonify, request
from datetime import datetime

from aurantia_webservice.core.decorators import arduino_registered
from aurantia_webservice.core.db import db
from aurantia_webservice.core.utils import get_json_message
from aurantia_webservice.models import Arduino, Data

from utils import (check_arduino_data_integrity, get_all_arduino_data,
                    convert_list_data_to_dict, check_register_data,
                    check_arduino_connection, check_all_arduino_connection,
                    clean_list_objects)


module_api = Blueprint('api', __name__, url_prefix='/api')


@module_api.route("/", methods = ['GET'])
def index():
    all_arduino = Arduino.query.all()
    result = clean_list_objects(all_arduino)
    resp = jsonify(results = result)
    resp.status_code = 200

    return resp

@module_api.route('/arduino-signal/', methods = ['POST'])
@arduino_registered
def arduino_signal_data():
    fields = request.form.to_dict()
    if check_arduino_data_integrity(fields):
        arduino = Arduino.query.filter_by(ip_address=fields['ip_address']).first()
        new_data = Data(
                luminosity = fields['luminosity'],
                temperature = fields['temperature'],
                bustling = bool(fields['bustling']),
                arduino_id = arduino.id)
        arduino.informations.append(new_data)
        return get_json_message(200, 'sucess')
    return get_json_message(404, 'integrity data error')

@module_api.route('/<int:arduino_id>/', methods = ['GET'])
def arduino_data(arduino_id):
    arduino = Arduino.query.filter_by(id=arduino_id).first()
    if arduino is not None:
        all_data = get_all_arduino_data(arduino_id)
        resp = convert_list_data_to_dict(all_data)
        resp.status_code = 200
        return resp
    return get_json_message(404, 'Arduino not found')

@module_api.route('/<int:arduino_id>/status/', methods = ['GET'])
def arduino_status(arduino_id):
    arduino = Arduino.query.filter_by(id=arduino_id).first()
    if arduino is not None:
        result = check_arduino_connection(arduino.ip_address)
        resp = jsonify(arduino_status=result)
        return resp
    return get_json_message(404, 'Arduino not found')

@module_api.route('/status/', methods = ['GET'])
def all_arduino_status():
    resp = check_all_arduino_connection()
    return resp

@module_api.route('/register-arduino/', methods = ['POST'])
def arduino_register():
    fields = request.form.to_dict()
    if check_register_data(fields):
        new_arduino = Arduino(
                name = fields['name'],
                ip_address = fields['ip_address']
            )
        db.session.add(new_arduino)
        db.session.commit()
        resp = jsonify(token=new_arduino.secret_key)
        resp.status_code = 200
        return resp
    return get_json_message(404, 'integrity data error')

