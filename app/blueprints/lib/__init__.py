#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 10/8 16:46
# @Author  : acdzh
# @File    : __init__.py
# @Software: PyCharm

from flask import Blueprint

lib = Blueprint('lib', __name__)

from app.blueprints.lib import empic
