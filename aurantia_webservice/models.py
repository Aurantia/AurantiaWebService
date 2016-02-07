#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import os

from aurantia_webservice.core.db import db

class Laboratory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(30), nullable=False)
    arduinos = db.relationship('Arduino', backref='laboratory',
                                lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Laboratory %r>' %(self.name)


class Arduino(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    name = db.Column(db.String(30), nullable=False)
    ip_address = db.Column(db.String(15), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime)
    secret_key = db.Column(db.String(16), unique=True, nullable=False)
    laboratory_id = db.Column(db.Integer, db.ForeignKey('laboratory.id'))
    informations = db.relationship('Data', backref='arduino',
                                lazy='dynamic')

    def __init__(self, name, ip_address, laboratory_id):
        self.name = name
        self.ip_address = ip_address
        self.laboratory_id = laboratory_id
        self.timestamp = datetime.datetime.now()
        self.secret_key = os.urandom(8).encode('hex')

    def __repr__(self):
        return '<Arduino %r>' %(self.ip_address)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    luminosity = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    bustling = db.Column(db.Boolean)
    timestamp = db.Column(db.DateTime)
    arduino_id = db.Column(db.Integer, db.ForeignKey('arduino.id'))
    
    def __init__(self, luminosity, temperature, bustling, arduino_id):
        self.luminosity = luminosity
        self.temperature = temperature
        self.bustling = bustling
        self.arduino_id = arduino_id
        self.timestamp = datetime.datetime.now()

    def __repr__(self):
        return '<Data of arduino %r>' %(self.arduino_id)