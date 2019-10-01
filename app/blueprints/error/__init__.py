from flask import Blueprint, make_response

error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def api_not_found(e):
    return make_response('[404]没有找到您想要的资源', 404)


@error.app_errorhandler(500)
def internal_server_error(e):
    return make_response('[500]服务器内部错误', 500)
