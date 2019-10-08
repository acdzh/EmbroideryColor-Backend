#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 10/8 23:28
# @Author  : acdzh
# @File    : __init__.py
# @Software: PyCharm

from flask import Blueprint

view = Blueprint('view', __name__)

from app.views import helloworld


@view.route('/', methods=['GET', 'POST'])
def index():
    return "<p>index page. <a href=\"/helloworld\">Hello world</a><p>"
