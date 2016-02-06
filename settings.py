#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = "4c2cc707e708b9b2ad8a5d427868d580e85ea3943912d916"
    SECURITY_PASSWORD_SALT = "3e5fade13026ad4d6121d428c6eb43adf078d1719d1f4615"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    #BCRYPT_LOG_ROUNDS = 13


class ProdutionConfig(Config):
    DEBUG=False


class StangingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    PORT = 2000


class TestingConfig(Config):
    TESTING = True