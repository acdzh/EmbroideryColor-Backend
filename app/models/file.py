from app import db
from config import config
import time


class File(db.Model):
    __tablename__ = 'files'
    fid = db.Column(db.Integer, primary_key=True, nullable=False)
    uid = db.Column(db.Integer)
    md5 = db.Column(db.String(200))
    src_name = db.Column(db.String(100))
    upload_time = db.Column(db.Integer)

    def __init__(self, _uid, _md5, _src_name):
        files = self.query.all()
        max_fid = 100000
        for i in files:
            if i.fid > max_fid:
                max_fid = i.fid
        self.fid = max_fid + 1
        self.uid = _uid
        self.md5 = _md5
        self.src_name = _src_name
        self.upload_time = int(time.time())

    def json(self):
        return {
            "fid": self.fid,
            "uid": self.uid,
            "md5": self.md5,
            "upload_time": self.upload_time,
            "current_name": self.get_current_name(),
            "src_name": self.src_name,
            "url": self.get_url(),
            "path": self.get_path()
        }

    def get_ext(self):
        return self.src_name.rsplit('.', 1)[1]

    def get_current_name(self):
        return "{}.{}".format(self.md5, self.get_ext())

    def get_src_name(self):
        return self.src_name

    def get_url(self):
        return "{}/{}".format(config['basic'].FILE_HOST, self.get_current_name())

    def get_path(self):
        return "{}/{}".format(config['basic'].FILE_DIR, self.get_current_name())
