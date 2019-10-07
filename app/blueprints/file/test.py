from app.blueprints.file import file
from app.models.file import File

from flask import jsonify


@file.route('/test', methods=['POST', 'GET'])
def usertest():
    files = File.query.all()
    us = []
    for i in files:
        us.append(i.json())
    return jsonify(us)
