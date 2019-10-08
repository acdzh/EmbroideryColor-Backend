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
    create_views(app)
    return app


def regist_blueprints(app):
    from app.blueprints.error import error
    from app.blueprints.file import file
    from app.blueprints.lib import lib
    from app.blueprints.user import user

    app.register_blueprint(error, url_prefix='/error')
    app.register_blueprint(file, url_prefix='/file')
    app.register_blueprint(lib, url_prefix='/lib')
    app.register_blueprint(user, url_prefix='/user')


def create_tables(app):
    from app.models.file import File
    from app.models.token import Token
    from app.models.user import User
    from app.models.verify import Verify
    db.create_all(app=app)


def create_views(app):
    from app.views import view
    app.register_blueprint(view, url_prefix='')

#
# app = create_app('development')
# create_views()
