import os
from forms import  AddForm , DelForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class ece(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return f"Student name: {self.name}"

############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

#now we'll have a view to add and list all students
@app.route('/add',methods=['GET','POST'])
#   Addition of student begins
def add_student():
    form=AddForm()
    
    if form.validate_on_submit():
        
        name=form.name.data
        new_student=ece(name)
        db.session.add(new_student)
        db.session.commit()
        
        return redirect(url_for('list_student'))
    
    return render_template('add.html',form=form)
 # Addition of students ends

@app.route('/list')
def list_student():
    # Grab a list of puppies from database.
    students=ece.query.all()
    return render_template('list.html', students=students)

@app.route('/delete', methods=['GET', 'POST'])
def del_student():
    form=DelForm()
    
    if form.validate_on_submit():
        id=form.id.data
        bacha=ece.query.get(id)
        db.session.delete(bacha)
        db.session.commit()
        
        return redirect(url_for('list_student'))
    
    return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
    





    
    
