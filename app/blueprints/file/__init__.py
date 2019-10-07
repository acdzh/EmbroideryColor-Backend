from flask import Blueprint

file = Blueprint('file', __name__)

from app.blueprints.file import test
from app.blueprints.file import upload
