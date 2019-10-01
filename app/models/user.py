from app import db


class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    sex = db.Column(db.Integer)
    is_verified = db.Column(db.Boolean)
    friend_ids = db.Column(db.JSON)
    other = db.Column(db.JSON)

    def __init__(self, _nick_name, _email):
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
        self.other = {}

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
            'error': self.other
        }

