from app.blueprints.user import user
from app.models.user import User
import random
import string
from flask import make_response, jsonify


@user.route('/usertest', methods=['POST', 'GET'])
def usertest():
    # tempname = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    # tempemail = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    # a = User(tempname, tempemail)
    # db.session.add(a)
    # db.session.commit()

    users = User.query.all()
    us = []
    for i in users:
        us.append(i.json())
    return jsonify(us)
