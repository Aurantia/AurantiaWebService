#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest
import os
import datetime
import json

from flask_testing import TestCase
from aurantia_webservice.core.app import app
from aurantia_webservice.core.db import db
from aurantia_webservice.modules.api.views import module_api
from aurantia_webservice.models import Arduino, Data

class TestViews(TestCase):

    def create_app(self):
        app.register_blueprint(module_api)
        app.config.from_object(os.environ["APP_TESTING"])
        return app

    def test_home_json(self):
        response = self.client.get("/api/")
        self.assertEquals(response.json, dict(hello="world",
                                                aurantia="project"))

    def test_arduino_signal(self):
        #create a Arduino object
        new_arduino = Arduino("Lab 01", "192.153.24.19")
        db.session.add(new_arduino)
        db.session.commit()

        #make a post request
        response = self.client.post("/api/arduino-signal/",
                                        data=dict(ip_address="192.153.24.19",
                                                    luminosity="530",
                                                        bustling="True",
                                                            temperature="27",
                                                            secret_key=new_arduino.secret_key),
                                        follow_redirects=True)
        result = json.loads(response.data)
        assert 'sucess' in result['message']

        #delete data tested
        delete_arduino = Arduino.query.filter_by(id=new_arduino.id).first()
        db.session.delete(delete_arduino)
        db.session.commit()

if __name__ == '__main__':
    unittest.main()