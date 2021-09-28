from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    id = IntegerField("Id of student is : ")
    name = StringField("Name of Student : ")
    major = StringField("Major of Student : ")
    level = StringField("level of Student : ")
    age = IntegerField("Age of Student : ")
    submit = SubmitField("Add Student :")

class DelForm(FlaskForm):
    id = IntegerField("Id no. of student to remove : ")
    submit = SubmitField("Remove Student : ")


class AddFaculty(FlaskForm):
    id = IntegerField("Id of Faculty : ")
    name = StringField("Name of Faculty : ")
    dept_id = IntegerField("Department ID : ")
    submit = SubmitField("Add Faculty :")

class AddEnrolled(FlaskForm):
    id = IntegerField("Id of Enrolled : ")
    name = StringField("Name of Enrolled : ")
    submit = SubmitField("Add Enrolled:")


class AddClass(FlaskForm):
    name = StringField("Name of Class : ")
    meet_at = StringField("MEET AT : ")
    room = StringField("Name of Room : ")
    id = IntegerField("Id of class is : ")
    submit = SubmitField("Add Class : ")


class AddCourse(FlaskForm):
    name = StringField("Course name : ")
    teacher = StringField("Course teach by : ")
    submit = SubmitField("Add Course : ")