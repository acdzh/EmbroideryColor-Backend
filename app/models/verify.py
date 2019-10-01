from app import db

class Verify(db.Model):
    __tablename__ = 'verifies'
    num = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(20), nullable=False)
    uid = db.Column(db.Integer, nullable=False, primary_key=True)

    def __init__(self, _num, _url, _uid):
        self.num = _num
        self.url = _url
        self.uid = _uid

    def __repr__(self):
        return self.json()

    def json(self):
        return {
            'num': self.num,
            'url': self.url,
            'uid': self.uid
        }

    def get_uid(self):
        return self.uid
