#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import socket
import json

from flask import jsonify

from aurantia_webservice.models import Arduino, Data, Laboratory

def check_arduino_data_integrity(dict_data):
    full_dict = (dict_data.has_key('ip_address') 
                    and dict_data.has_key('bustling')
                        and dict_data.has_key('luminosity')
                            and dict_data.has_key('temperature'))

    return full_dict

def check_register_data(dict_data):
    return dict_data.has_key('name') and dict_data.has_key('ip_address')

def get_all_arduino_laboratory(lab_id):
    result = Arduino.query.filter_by(laboratory_id=lab_id).all()
    return result

def get_all_arduino_data(arduino_id):
    result = Data.query.filter_by(arduino_id=arduino_id).order_by(Data.timestamp.desc()).all()
    return result

def clean_list_objects(list_data):
    list_result = []
    for data in list_data:
        data.timestamp = str(data.timestamp)
        result_dict = data.__dict__
        del result_dict['_sa_instance_state']
        list_result.append(result_dict)
    return list_result

def convert_list_data_to_dict(data):
    cleaned_data = clean_list_objects(data)
    return jsonify(results = cleaned_data)

def check_arduino_connection(ip_address):
    socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = None
    try:
        socket_object.connect((ip_address, 80))
        result = True
    except:
        result = False
    finally:
        socket_object.close()
    return result

def check_list_arduino_connection(list_objects):
    list_result = []
    for arduino in list_objects:
        arduino_status = check_arduino_connection(arduino.ip_address)
        dict_temp = {
            'id' : arduino.id,
            'ip_address' : arduino.ip_address,
            'arduino_status' : arduino_status
        }
        list_result.append(dict_temp)

    return list_result
