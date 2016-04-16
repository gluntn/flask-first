from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
 user = {'nickname': 'Miguel'}
 posts = [
 { 
  'author':  {'nickname': 'John'},
  'body': 'Beautiful day!'
 },
 {
  'author': {'nickname': 'Susan'},
  'body': 'Cool movie'
 }
 ]
 return render_template('index.html',
   user=user,
   posts=posts)
