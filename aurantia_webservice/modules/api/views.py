#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask import Blueprint, jsonify, request
from datetime import datetime

from aurantia_webservice.core.decorators import arduino_registered
from aurantia_webservice.core.db import db
from aurantia_webservice.core.utils import get_json_message
from aurantia_webservice.models import Arduino, Data, Laboratory

from utils import (check_arduino_data_integrity, get_all_arduino_data,
                    convert_list_data_to_dict, check_register_data,
                    check_arduino_connection, check_list_arduino_connection,
                    clean_list_objects, get_all_arduino_laboratory)


module_api = Blueprint('api', __name__, url_prefix='/api')


@module_api.route("/arduino/all/", methods = ['GET'])
def index():
    all_arduino = Arduino.query.all()
    result = clean_list_objects(all_arduino)
    resp = jsonify(results = result, total_arduino=len(all_arduino))
    resp.status_code = 200

    return resp

@module_api.route('/arduino/all/status/', methods = ['GET'])
def all_arduino_status():
    all_arduino = Arduino.query.all()
    result = check_list_arduino_connection(all_arduino)
    resp = jsonify(results = result)
    resp.status_code = 200
    return resp

@module_api.route('/lab/<int:lab_id>/', methods = ['GET'])
def lab_arduino(lab_id):
    laboratory = Laboratory.query.filter_by(id=lab_id).first()
    if laboratory is not None:
        all_arduino = get_all_arduino_laboratory(lab_id)
        resp = jsonify(results = clean_list_objects(all_arduino),
                        lab_name=laboratory.name, lab_id=laboratory.id,
                        total_arduino=len(all_arduino))
        resp.status_code = 200

        return resp
    return get_json_message(404, 'Lab not found.')

@module_api.route('/lab/<int:lab_id>/status/', methods = ['GET'])
def lab_arduino_status(lab_id):
    laboratory = Laboratory.query.filter_by(id=lab_id).first()
    if laboratory is not None:
        all_arduino = get_all_arduino_laboratory(lab_id)
        result = check_list_arduino_connection(all_arduino)
        resp = jsonify(lab_name=laboratory.name, lab_id=laboratory.id,
                        all_arduino = result)
        resp.status_code = 200

        return resp
    return get_json_message(404, 'Lab not found.')

@module_api.route('/arduino/<int:arduino_id>/', methods = ['GET'])
def arduino_data(arduino_id):
    arduino = Arduino.query.filter_by(id=arduino_id).first()
    if arduino is not None:
        all_data = get_all_arduino_data(arduino_id)
        resp = convert_list_data_to_dict(all_data)
        resp.status_code = 200
        return resp
    return get_json_message(404, 'Arduino not found')

@module_api.route('/arduino/<int:arduino_id>/status/', methods = ['GET'])
def arduino_status(arduino_id, key):
    arduino = Arduino.query.filter_by(id=arduino_id).first()
    if arduino is not None:
        result = check_arduino_connection(arduino.ip_address)
        resp = jsonify(arduino_status=result)
        return resp
    return get_json_message(404, 'Arduino not found')

@module_api.route('/arduino/register/', methods = ['POST'])
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

@module_api.route('/arduino/signal/', methods = ['POST'])
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