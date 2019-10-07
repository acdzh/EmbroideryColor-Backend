import json
from app import db
from app.blueprints.user import user
from app.models.user import User

from flask import jsonify, request


def is_email_exist(_email):
    users = User.query.all()
    emails = []
    for i in users:
        emails.append(i.get_email())
    if _email in emails:
        return True
    else:
        return False


@user.route('/regist', methods=['POST'])
def create_user():
    try:
        body = json.loads(request.data)
    except:
        return jsonify({'code': 4, 'msg': 'json not correct'})
    for i in ('email', 'password'):
        if i not in body.keys():
            return jsonify({'code': 1, 'msg': 'need key: {}'.format(i)})
    if is_email_exist(body['email']):
        return jsonify({'code': 2, 'msg': 'email has exist'})

    email = body["email"]
    password = body["password"]
    if 'nickname' in body.keys():
        nickname = body["nickname"]
    else:
        nickname = 'NaN'

    try:
        new_user = User(_email=email, _password=password, _nick_name=nickname)
        uid = new_user.get_uid()
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            'code': 0,
            'msg': 'success',
            'data': {'uid': uid, 'email': email, 'nickname': nickname}
        })

    except:
        return jsonify({'code': 3, 'msg': 'server error: insert user failed'})
