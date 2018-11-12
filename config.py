"""Configuration file for running the app in staging and production"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Generic base class"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

class ProductionConfig(Config):
    """Production Class - Heroku"""
    DEBUG = False

class StagingConfig(Config):
    """Staging Class - N/A"""
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    """Dev Class - Local Workstation"""
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    """Test Class - Py.test data"""
    TESTING = True