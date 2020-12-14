from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo

class CommentForm(FlaskForm):
    email=StringField('Your email ',validators=[Required(),Email()])
    name=StringField("Your name",validators=[Required()])
    comment=TextAreaField("Comment",validators=[Required()])
    submit=SubmitField("Submit")

class AdminBlog(FlaskForm):

    title=StringField("Title",validators=[Required()])
    body=TextAreaField("Blog Body")
    submit=SubmitField("Submit")

class DeleteBlog(FlaskForm):
    delete=SubmitField("Delete this Blog")

class DeleteComment(FlaskForm):
    delete1=SubmitField("Delete")

class UpdateProfile(FlaskForm):
    about=TextAreaField("Tell us about you ",validators=[Required()])
    occupation=StringField("What is you current occupation",validators=[Required()])
    submit=SubmitField("Save")
