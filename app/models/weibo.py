#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 10/17 16:21
# @Author  : acdzh
# @File    : weibo.py
# @Software: PyCharm

from app import db
from config import config


class Weibo(db.Model):
    __tablename__ = 'weibos'
    wid = db.Column(db.Integer, primary_key=True, unique=True)
    uid =