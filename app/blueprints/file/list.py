import json

from app.blueprints.file import file
from app.models.file import get_all_files_by_uid
from app.models.token import get_uid_by_tokenid

from flask import jsonify, request


@file.route('/list', methods=['POST'])
def file_list():
    body = json.dumps(request.data)
    uid = get_uid_by_tokenid(body["tokenid"])
    if uid == -1:
        return jsonify({'code': 2, 'msg': 'no such user'})
    files = get_all_files_by_uid()
    return jsonify({'code': 0, 'msg': 'success', 'data': files})
