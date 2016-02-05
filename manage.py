#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from flask.ext.script import Manager, Command
from flask.ext.migrate import Migrate, MigrateCommand

from aurantia_webservice.core.app import app
from aurantia_webservice.core.db import db
from aurantia_webservice.commands import Server

import os

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('runserver', Server())
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()