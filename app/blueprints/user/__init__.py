from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from app.models.token import Token
import json

import random
import string
import time

user = Blueprint('user', __name__)

from app.blueprints.user import usertest, verify


def is_email_exist(_email):
    users = User.query.all()
    emails = []
    for i in users:
        emails.append(i.get_email())
    if _email in emails:
        return True
    else:
        return False


@user.route('/new', methods=['POST'])
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


@user.route('/login', methods=['POST'])
def login():
    try:
        body = json.loads(request.data)
    except:
        return jsonify({'code': 4, 'msg': 'json not correct'})

    if "password" not in body.keys():
        return jsonify({'code': 1, 'msg': 'need key: password'})
    else:
        password = body["password"]

    if "uid" in body.keys():
        uid = body["uid"]
        users = User.query.filter_by(uid=uid).all()
    elif "email" in body.keys():
        email = body["email"]
        users = User.query.filter_by(email=email).all()
    else:
        return jsonify({'code': 1, 'msg': 'need uid or email'})

    if len(users) != 1:
        return jsonify({'code': 2, 'msg': 'can not find this user'})
    uid = users[0].get_uid()

    if not users[0].check_passwd(password):
        return jsonify({'code': 5, 'msg': 'password not correct'})

    try:
        tokenid = str(int(time.time())) + ''.join(random.sample(string.ascii_letters + string.digits, 15))
        print(tokenid)
        new_token = Token(_tokenid=tokenid, _uid=uid)
        db.session.add(new_token)
        db.session.commit()
    except:
        return jsonify({'code': 3, 'msg': 'new token error'})

    return jsonify({'code': 0, 'msg': 'success', 'data': {
        'tokenid': tokenid,
        'user': users[0].json()
    }})

@user.route('/logout', methods=['POST'])
def logout():
    try:
        body = json.loads(request.data)
    except:
        return jsonify({'code': 4, 'msg': 'json not correct'})

    if "tokenid" not in body.keys():
        return jsonify({'code': 1, 'msg': 'need key: tokenid'})
    else:
        tokenid = str(body["tokenid"])

    tokens = Token.query.filter_by(tokenid=tokenid).all()

    if len(tokens) == 0:
        return jsonify({'code': 2, 'msg': 'can not find token: {}'.format(tokenid)})

    try:
        for i in tokens:
            db.session.delete(i)
        db.session.commit()
    except:
        return jsonify({'code': 3, 'msg': 'del token error'})

    return jsonify({'code': 0, 'msg': 'success', 'data': {
        'tokenid': tokenid
    }})