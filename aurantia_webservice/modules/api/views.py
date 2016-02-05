#!/usr/bin/env python
# -*- encoding: utf-8 -*-


from flask import Blueprint, jsonify

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
