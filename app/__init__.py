from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    print(config_name)
    app.config.from_object(config[config_name])
    db.init_app(app)
    create_tables(app)
    regist_blueprints(app)
    return app


def regist_blueprints(app):
    from app.blueprints.user import user
    from app.blueprints.error import error
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(error, url_prefix='/error')


def create_tables(app):
    from app.models.user import User
    from app.models.verify import Verify
    from app.models.token import Token
    db.create_all(app=app)


def create_views():
    from app.views import helloworld


app = create_app('development')

create_views()
