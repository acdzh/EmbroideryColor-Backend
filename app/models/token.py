from app import db


def get_uid_by_tokenid(_tokenid):
    try:
        return Token.query.filter_by(tokenid=_tokenid).first().get_uid()
    except:
        return -1


class Token(db.Model):
    __tablename__ = "tokens"
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
