'''
Created on Jan 10, 2017

@author: hanif
'''

from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database


app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

@app.route('/')
def index():
    data = db.read(None)

    return str(data)

@app.route('/add/')
def add():
    return str(data)

@app.route('/addpost', methods = ['POST', 'GET'])
def upoloadpost():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A post has been added")
        else:
            flash("A post can not be added")

        return str("Good Job")
    else:
        return str("Failed")

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return str(data)

@app.route('/updatepost', methods = ['POST'])
def updatepost():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A post has been updated')

        else:
            flash('A post can not be updated')

        session.pop('update', None)

         return str("Good Job")
    else:
        return str("Failed")

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        flash('there is nothing to delete')
    else:
        session['delete'] = id
        return str(data)

@app.route('/deletepost', methods = ['POST'])
def deletepost():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A post has been deleted')

        else:
            flash('A post can not be deleted')

        session.pop('delete', None)

          return str("Good Job")
    else:
        return str("Failed")



if __name__ == '__main__':
    app.run(port=3434, host="0.0.0.0")
