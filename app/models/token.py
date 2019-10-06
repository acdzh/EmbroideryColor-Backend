from app import db

class Token(db.Model):
    __lablename__ = "tokens"
    tokenid = db.Column(db.String(25), primary_key=True)
    uid = db.Column(db.Integer)

    def __init__(self, _tokenid, _uid):
        self.tokenid = _tokenid
        self.uid = _uid

    def json(self):
        return {
            'tokenid': self._id,
            'uid': self.uid
        }

    def get_tokenid(self):
        return self.tokenid

    def get_uid(self):
        return self.uid