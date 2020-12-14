from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from .import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(250),index=True)
    email=db.Column(db.String(250),unique=True,index=True)
    pass_secure=db.Column(db.String(250))
    profile=db.Column(db.String(250))
    about=db.Column(db.String(250))
    occupation=db.Column(db.String(250))

    @property
    def password(self):
        raise AttributeError("You can not read this")

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f"User {self.username}"

class Blogs(db.Model):
    __tablename__='blogs'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String())
    body=db.Column(db.String())



class Comments(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String())
    username=db.Column(db.String())
    comment=db.Column(db.String())
    blog_id=db.Column(db.Integer)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    

    def save_comments(self):
        db.session.add(self);
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments=Comments.query.filter_by(blog_id=id).all()
        return comments

class Quote:
    def __init__(self,quote,author):
        self.quote=quote
        self.author=author




class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
