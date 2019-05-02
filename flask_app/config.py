import os


class Config:
    """
    Base Configuration
    """

    SECRET_KEY = os.getenv('SECRET_KEY', 'testkey')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "api.log"  # where logs are outputted to


class DevelopmentConfig(Config):
    """
    Development Configuration - default config
    """

    url = (
        "sqlite:////tmp/test.db"
    )  # set the URI to call get_pg_url() once you have `creds.ini` setup
    SQLALCHEMY_DATABASE_URI = url
    DEBUG = True


class ProductionConfig(Config):
    """
    Production Configuration


    You can update it to use a `creds.ini` file or anything you want.

    Requires the environment variable `FLASK_ENV=prod`
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    )
    DEBUG = False


class TestConfig(Config):
    """
    Testing Configuration

    """

    SQLALCHEMY_DATABASE_URI = (
        "sqlite:////tmp/test.db"
    )
    DEBUG = True


# way to map the value of `FLASK_ENV` to a configuration
config = {"dev": DevelopmentConfig,
          "prod": ProductionConfig, "test": TestConfig}
