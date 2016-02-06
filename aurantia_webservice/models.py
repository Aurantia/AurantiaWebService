#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime

from aurantia_webservice.core.db import db


class Arduino(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    name = db.Column(db.String(30), nullable=False)
    ip_address = db.Column(db.String(15), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime)
    informations = db.relationship('Data', backref='arduino',
                                lazy='dynamic')

    def __init__(self, name, ip_address, timestamp=None):
        self.name = name
        self.ip_address = ip_address
        self.timestamp = datetime.datetime.now()

    def __repr__(self):
        return '<Arduino %r>' %(self.ip_address)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    luminosity = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    bustling = db.Column(db.Boolean)
    date_log = db.Column(db.DateTime)
    arduino_id = db.Column(db.Integer, db.ForeignKey('arduino.id'))
    
    def __init__(self, luminosity, temperature, bustling, arduino_id,
                    date_log=None):
        self.luminosity = luminosity
        self.temperature = temperature
        self.bustling = bustling
        self.arduino_id = arduino_id
        self.date_log = datetime.datetime.now()

    def __repr__(self):
        return '<Data of arduino %r>' %(self.arduino_id)