class BaseConfig(object):
    """Base configuration"""
    TESTING = False
    SECRET_KEY = 'my_precious'


class DevelopmentConfig(BaseConfig):
    """Develoment configuration"""
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
