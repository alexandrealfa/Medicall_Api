from environs import Env

env = Env()
env.read_env()


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    CONFIG_NAME = 'development'
    SQLALCHEMY_DATABASE_URI = env("DB_URI_DEV")
    TESTING = False
    JWT_SECRET_KEY = env("SECRET_KEY")


class ProductionConfig(Config):
    ...


class TestConfig(Config):
    CONFIG_NAME = 'test'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = env("DB_URI_TEST")


config_selector = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestConfig,
}