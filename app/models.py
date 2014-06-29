from datetime import datetime
from app import db


class Post(db.Model):
    __tablename __ = 'Post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    text = db.Column(db.String(500), nullable = False)
    post_date = db.Column(db.Date, nullable=False)
    moddified_date = db.Column(db.Date)

    def __init__(self, title, text, post_date, modified_date):
        self.title = title
        self.text = text
        self.post_date = datetime.utcnow()