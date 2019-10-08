#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 10/8 16:48
# @Author  : acdzh
# @File    : empic.py
# @Software: PyCharm

import hashlib
import pathlib

from app.blueprints.lib import lib
from app.models.token import get_uid_by_tokenid
from app.lib.empic import get_pic
from config import config
from flask import request, jsonify


@lib.route('/empic', methods=['POST'])
def get_empic():
    if request.method == 'POST':
        f = request.files['file']
        name = "{}.{}".format(hashlib.md5(f.read()).hexdigest(), f.filename.split('.')[-1])
        src_path = "./static/lib/empic/src/{}".format(name)
        if pathlib.Path(src_path).is_file():
            pass
        else:
            f.seek(0)
            f.save(src_path)

        args = {
            "width_dimension": 20,
            "tilers_count": 50,
            "tiler_size": 30
        }
        for i in ('width_dimension', 'tilers_count', 'tiler_size'):
            if i in request.form:
                args[i] = int(request.form[i])
        try:
            pic_name = get_pic(
                srcfile=src_path, picpath="./static/lib/empic/pic",
                width_dimension=args['width_dimension'],
                TILERS_COUNT=args['tilers_count'], TILER_SIZE=args['tiler_size'])
            return jsonify({'code': 0, 'msg': 'success', 'data': {'url': "{}/empic/pic/{}".format(config['basic'].LIB_HOST, pic_name)}})
        except:
            return jsonify({'code': 3, 'msg': 'get pic fail'})

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