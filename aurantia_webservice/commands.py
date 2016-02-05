#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask.ext.script import Command

from aurantia_webservice import create_app


class Server(Command):

    def run(self):
        app = create_app()
        app.run(port=8080)