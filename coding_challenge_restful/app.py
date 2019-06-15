from flask import Flask
from flask_migrate import Migrate

from coding_challenge_restful.extensions import db
from coding_challenge_restful.flask_restful_api import restful_api


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    migrate = Migrate(app=app, db=db)
    migrate.init_app(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    restful_api(app)
    return app
