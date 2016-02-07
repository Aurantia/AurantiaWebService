#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import random

from flask.ext.script import Command, Option
from flask.ext.script.commands import InvalidCommand

from aurantia_webservice import create_app
from aurantia_webservice.core.db import db
from aurantia_webservice.core.utils import generate_random_ip

from models import Arduino, Data, Laboratory


class Server(Command):

    def run(self):
        app = create_app()
        app.run(port=8080)

class PopulateDatabase(Command):

    option_list = (
            Option('--table', '-t', dest='table'),
            Option('--reference', '-r', dest='reference'),
        )

    def run(self, table, reference):
        tables = ["arduino", "data"]
        if table in tables and reference is None:
            raise InvalidCommand("Options table and reference are incompatible")

        if table == "laboratory":
            lab_number = random.randint(0, 200)
            new_laboratory = Laboratory(name="Lab " + str(lab_number))
            print new_laboratory.name
            db.session.add(new_laboratory)
            db.session.commit()

        if table == "arduino":
            arduino_number = random.randint(0, 200)
            new_arduino = Arduino(
                name = "Arduino " + str(arduino_number),
                ip_addres = generate_random_ip(),
                laboratory_id = reference
            )

            db.session.add(new_arduino)
            db.session.commit()

        if table == "data":
            luminosity = random.randint(50, 1000)
            temperature = random.randint(15, 30)
            bustling = random.choice([True, False])
            new_data = Data(
                luminosity =  luminosity,
                temperature =  temperature,
                bustling = bustling,
                arduino_id = reference
            )

            db.session.add(new_data)
            db.session.commit()

