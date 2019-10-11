import json, hashlib, pathlib

from app import db
from app.blueprints.user import user
from app.models.user import User
from app.models.token import get_uid_by_tokenid

from config import config

from flask import jsonify, request


def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'JPG', 'PNG', 'gif', 'GIF', 'JPEG'}
    return '.' in filename and filename.rsplit('.', 1)[1] in allowed_extensions


@user.route('/modify', methods=['POST'])
def modify_info():
    try:
        body = json.loads(request.data)
    except:
        return jsonify({'code': 4, 'msg': 'json not correct'})

    if "tokenid" not in body.keys():
        return jsonify({'code': 1, 'msg': 'need key: tokenid'})
    else:
        tokenid = str(body["tokenid"])
    try:
        t_user = User.query.filter_by(uid=get_uid_by_tokenid(tokenid)).first()
    except:
        return jsonify({'code': 2, 'msg': 'no such user'})

    try:
        t_user.update(body)
        print(t_user.json())
        db.session.commit()
    except:
        return jsonify({'code': 3, 'msg': 'commit changes fail'})

    return jsonify({'code': 0, 'msg': 'success', 'data': {
        'tokenid': tokenid,
        'user': t_user.json()
    }})


@user.route('/modify/avatar', methods=['GET', 'POST'])
def update_avatar():
    if request.method == 'POST':
        f = request.files['file']
        if "name" in request.form:
            name = request.form["name"]
        else:
            name = f.filename
        if allowed_file(name):
            md5 = hashlib.md5(f.read()).hexdigest()
            real_name = "{}.{}".format(md5, name.rsplit('.', 1)[1])
            if pathlib.Path(config["basic"].AVATAR_DIR + "/{}".format(real_name)).is_file():
                pass
            else:
                f.seek(0)
                f.save(config["basic"].AVATAR_DIR + "/{}".format(real_name))
            try:
                uid = get_uid_by_tokenid(request.form['tokenid'])
                t_user = User.query.filter_by(uid=uid).first()
                t_user.avatar = config["basic"].AVATAR_HOST + "/{}".format(real_name)
                db.session.commit()
                return jsonify({'code': 0, 'msg': 'success', 'data': {
                    'uid': uid,
                    'url': config["basic"].AVATAR_HOST + "/{}".format(real_name)
                }})
            except:
                return jsonify({'code': 3, 'msg': 'commit changes fail'})
        else:
            return jsonify({'code': 1, 'msg': 'file extension name illegal! open receive pics'})
    if request.method == 'GET':
        return '''
            <!doctype html>
            <title>Upload new avatar - test page</title>
            <form action="" method=post enctype=multipart/form-data>
                 <input type=file name=file>
                 <input name=filename>
                 <input name=tokenid>
                 <input type=submit value=Upload>
            </form>
        '''
