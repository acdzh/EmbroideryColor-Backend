import hashlib, pathlib

from app import db
from app.blueprints.file import file
from app.models.file import File
from app.models.token import Token

from config import config
from flask import jsonify, request


@file.route('/upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        name = request.form['name']
        md5 = hashlib.md5(f.read()).hexdigest()
        real_name = "{}.{}".format(md5, name.rsplit('.', 1)[1])
        if pathlib.Path(config["basic"].FILE_DIR + "/{}".format(real_name)).is_file():
            pass
        else:
            f.seek(0)
            f.save(config["basic"].FILE_DIR + "/{}".format(real_name))
        try:
            uid = Token.query.filter_by(tokenid=request.form['tokenid']).first().get_uid()
            new_file = File(_uid=uid, _md5=md5, _src_name=name)
            print(new_file.json())
            db.session.add(new_file)
            db.session.commit()
            return jsonify(new_file.json())
        except:
            return jsonify({'code': 3, 'msg': 'commit changes fail'})

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