#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask.ext.script import Command

from aurantia_webservice import create_app
from aurantia_webservice.core.db import db
from aurantia_webservice.core.utils import generate_random_ip

from models import Arduino, Data


class Server(Command):

    def run(self):
        app = create_app()
        app.run(port=8080)

class PopulateDatabase(Command):

    def run(self):
        new_arduino = Arduino("Lab", generate_random_ip())
        first_data = Data(
                luminosity = 654,
                temperature = 20.4,
                bustling = True,
                arduino_id = new_arduino.id
            )
        second_data = Data(
                luminosity = 230,
                temperature = 28.4,
                bustling = False,
                arduino_id = new_arduino.id
            )
        new_arduino.informations.append(first_data)
        new_arduino.informations.append(second_data)
        db.session.add(new_arduino)
        db.session.commit()
