class BaseConfig():
    TESTING = False


class DevelopmentConfig(BaseConfig):
    pass

class TesingConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    pass

