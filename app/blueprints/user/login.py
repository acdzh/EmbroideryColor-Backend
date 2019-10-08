import json, time, random, string

from app import db
from app.blueprints.user import user
from app.models.user import User
from app.models.token import Token

from flask import jsonify, request


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
