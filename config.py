from environs import Env

env = Env()
env.read_env()


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = env("DB_URI_DEV")


class ProductionConfig(Config):
    ...


class TestConfig(Config):
    ...


config_selector = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "test": TestConfig,
}