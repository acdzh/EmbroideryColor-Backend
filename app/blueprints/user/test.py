from app.blueprints.user import user
from app.models.user import User

from flask import jsonify


@user.route('/test', methods=['POST', 'GET'])
def test():
    users = User.query.all()
    us = []
    for i in users:
        us.append(i.json())
    return jsonify(us)
