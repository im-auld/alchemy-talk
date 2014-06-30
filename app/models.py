from datetime import datetime
# from app import db


# class Post(db.Model):
#     __tablename__ = 'Post'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(50), unique=True, nullable=False)
#     text = db.Column(db.String(500), nullable = False)
#     post_date = db.Column(db.Date, nullable=False)
#     moddified_date = db.Column(db.Date)

#     def __init__(self, title, text):
#         self.title = title
#         self.text = text
#         self.post_date = datetime.utcnow()

#     def __repr__(self):
#         return '{post.title} - posted on: {post.post_date}'.format(post=self)

#     def modify_post(self, title, text):
#         self.title = title
#         self.text = text
#         self.moddified_date = datetime.utcnow()