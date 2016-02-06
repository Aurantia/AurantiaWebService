#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest

from flask_testing import TestCase
from aurantia_webservice.core.app import app
from aurantia_webservice.modules.api.views import module_api

class TestViews(TestCase):

    def create_app(self):
        app.register_blueprint(module_api)
        return app

    def test_home_json(self):
        response = self.client.get("/api/")
        self.assertEquals(response.json, dict(hello="world", aurantia="project"))

if __name__ == '__main__':
    unittest.main()