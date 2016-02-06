#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from flask import Blueprint, jsonify, request
from datetime import datetime

from aurantia_webservice.core.decorators import arduino_registered
from aurantia_webservice.core.utils import get_json_message
from aurantia_webservice.models import Arduino, Data

from utils import check_arduino_data_integrity


module_api = Blueprint('api', __name__, url_prefix='/api')


@module_api.route("/", methods = ['GET'])
def index():
    """
        This method only accept GET requests and return a json.
    """
    data = {
        'hello'  : 'world',
        'aurantia' : 'project'
    }
    resp = jsonify(data)
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

