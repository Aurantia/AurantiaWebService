#!/usr/bin/env python
# -*- coding:utf-8 -*-

from aurantia_webservice.core.db import db


class Arduino(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    name = db.Column(db.String(30), nullable=False)
    ip_address = db.Column(db.String(15), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime)
    informations = db.relationship('Data', backref='arduino',
                                lazy='dynamic')

    def __repr__(self):
        return '<Arduino %r>' %(self.ip_address)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    luminosity = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    bustling = db.Column(db.Boolean)
    date_log = db.Column(db.DateTime)
    arduino_id = db.Column(db.Integer, db.ForeignKey('arduino.id'))
    
    def __repr__(self):
        return '<Data of arduino %r>' %(self.arduino_id)