from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Chris'}
    posts = [
        {
            'author': {'username': 'Chris'},
            'body': """
Decided that I wanted to try and do more blogging about stuff that I learn, so I though what better way to start than by
making the blog site from scratch in python to learn some web development in the process. Plus 
https://airflow.apache.org/Airflow uses Flask for it's UI I believe, so it'll be a good learning
experience for that to.
"""
        },
        {
            'author': {'username': 'Chris'},
            'body': 'Hopefully I actually make more blog posts...'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

