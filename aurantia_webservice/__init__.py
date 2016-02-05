#!/usr/bin/env python
# -*- coding:utf-8 -*-

from aurantia_webservice.core.app import app
from aurantia_webservice.modules.api.views import module_api


def create_app():
	"""
		Return a object of flask configured and register blueprints.
	"""
	app.register_blueprint(module_api)
	return app