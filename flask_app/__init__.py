import os

from flask import Flask, request
import logging
from .config import config
from .database import Base
from flask_migrate import Migrate


class RequestFormatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    env = os.environ.get("FLASK_ENV", "dev")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(config[env])
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # logging
    formatter = RequestFormatter(
        "%(asctime)s %(remote_addr)s: requested %(url)s: %(levelname)s in\
        [%(module)s: %(lineno)d]: %(message)s"
    )
    if app.config.get("LOG_FILE"):
        fh = logging.FileHandler(app.config.get("LOG_FILE"))
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        app.logger.addHandler(fh)

    strm = logging.StreamHandler()
    strm.setLevel(logging.DEBUG)
    strm.setFormatter(formatter)

    app.logger.addHandler(strm)
    app.logger.setLevel(logging.DEBUG)

    from flask_app.database import db_session

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    migrate = Migrate(app, Base)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello/')
    def hello():
        app.logger.debug('Hello, World!')
        return 'Hello, World!'

    from flask_app.views import user
    app.register_blueprint(user.bp)

    return app
