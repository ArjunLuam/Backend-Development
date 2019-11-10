from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name=StringField('Name of Student:')
    submit=SubmitField('AddStudent')
    
    
    

class DelForm(FlaskForm):
    id=IntegerField('id of student to be removed:')
    submit=SubmitField('Remove Student')
    
    