from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Chris'}
    posts = [
        {
            'author': {'username': 'Emily'},
            'body': 'Beautiful day in Oxford!'
        },
        {
            'author': {'username': 'Alex'},
            'body': 'The new Star Trek is so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

