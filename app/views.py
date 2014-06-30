from flask import render_template
from app import app
#from models import Post


@app.route('/')
@app.route('/index')
def index():
    #posts = Post.query.all()
    return render_template('index.html', #posts=posts
        )