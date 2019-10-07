from app import db
from app import config
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(80))
    password = db.Column(db.String(255), nullable=True)
    email = db.Column(db.String(120), unique=True)
    sex = db.Column(db.Integer)
    is_verified = db.Column(db.Boolean)
    friend_ids = db.Column(db.JSON)
    avatar = db.Column(db.String(255))
    other = db.Column(db.JSON)

    def __init__(self, _email, _password, _nick_name='NaN', _sex=2):
        users = self.query.all()
        max_uid = 10000
        for i in users:
            if i.uid > max_uid:
                max_uid = i.uid
        self.uid = max_uid + 1
        self.nick_name = _nick_name
        self.email = _email
        self.sex = 2
        self.is_verified = False
        self.friend_ids = []
        self.avatar = config['HOST'] + "/avatar/default.png"
        self.other = {}

        self.password = generate_password_hash(_password)

    def __repr__(self):
        return self.json()

    def json(self):
        return {
            'uid': self.uid,
            'nick_name': self.nick_name,
            'email': self.nick_name,
            'sex': self.sex,
            'is_verified': self.is_verified,
            'friend_ids': self.friend_ids,
            'avatar': self.avatar,
            'other': self.other
        }

    def json_with_password(self):
        j = self.json()
        j["password"] = self.password
        return j

    def get_uid(self):
        return self.uid

    def get_passwd(self):
        return self.password

    def get_email(self):
        return self.email

    def get_avarat(self):
        return self.avatar

    def check_passwd(self, _password):
        return check_password_hash(self.password, _password)

    def update(self, _info):
        if 'avatar' in _info.keys():
            self.avatar = _info["avatar"]
        if 'nick_name' in _info.keys():
            self.nick_name = _info["nick_name"]
        if 'sex' in _info.keys():
            self.sex = _info["sex"]
        if 'other' in _info.keys():
            self.other = {**self.other, **_info["other"]}

