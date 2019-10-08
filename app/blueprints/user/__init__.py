from flask import Blueprint

user = Blueprint('user', __name__)

from app.blueprints.user import login
from app.blueprints.user import modify_info
from app.blueprints.user import regist
from app.blueprints.user import test
from app.blueprints.user import verify
