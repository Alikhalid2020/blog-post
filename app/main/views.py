from . import main
from flask import render_template,redirect,url_for,flash,request,abort
from .forms import CommentForm,AdminBlog,DeleteBlog,DeleteComment,UpdateProfile
from .. import db,photos
# import markdown2
from ..models import Blogs,Comments,User
from ..request import get_quote
# from ..email import mail_message



@main.route("/",methods=['POST','GET'])
def index():
    quote=get_quote()
    title="Blog"
    message="Mental Health Wellness"
    blogs=Blogs.query.all()
    top_blog=Blogs.query.all()
    top_blog.reverse()
    topBlog=top_blog[0:1]
    commento=Comments.query.filter_by(blog_id=500).all()
    form = CommentForm()
    if form.validate_on_submit():
        comments=Comments(blog_id=500,email=form.email.data,username=form.name.data,comment=form.comment.data)
        comments.save_comments()
        return redirect(url_for('main.index'))
    return render_template("index.html",commento=commento,topBlog=topBlog,quote=quote,message=message,title=title,comments=form,blogs=blogs)

@main.route("/new_blog",methods=["POST","GET"])
def new_blog():
    #query all emails
    emails=Comments.query.all()
    all_emails=[]
    for emal in emails:
        all_emails.append(emal.email)


    form=AdminBlog()
    if form.validate_on_submit():
        blog=Blogs(title=form.title.data,body=form.body.data)
        db.session.add(blog)
        db.session.commit()
        mail_message("Hello A new Blog has been posted","email/welcome_user","")
        return redirect(url_for('main.index'))

    title="Write a blog"
    return render_template("new_blog.html",title=title,newBlog=form,all_emails=all_emails)

@main.route("/read_blog/title/<int:id>/",methods=['GET','POST'])
def read_blog(id):
    blog_id=id
    title="Blog"
    message="Welcome to my Blog"
    blog=Blogs.query.filter_by(id=id).first()
    blogs=Blogs.query.all()
    data=blog.title
    form = CommentForm()

    if form.validate_on_submit():
        comments=Comments(blog_id=id,email=form.email.data,username=form.name.data,comment=form.comment.data)
        comments.save_comments()
        return redirect(url_for('main.read_blog',id=blog_id))



    format_blog=markdown2.markdown(blog.body,extras=["code-friendly", "fenced-code-blocks"])

    blog_comment=Comments.query.filter_by(blog_id=id).all()


    del_form=DeleteBlog()
    dele=Blogs.query.filter_by(id=id).first()
    if del_form.validate_on_submit():

        db.session.delete(dele)
        db.session.commit()
        
        return redirect(url_for('main.index'))



    del_comment=DeleteComment()

    if del_comment.validate_on_submit():
        dele_com=Comments.query.filter_by(blog_id=id).first()
        db.session.delete(dele_com)
        db.session.commit()

        return redirect(url_for('main.read_blog',id=blog_id))



    return render_template("read_blog.html",deleteform=del_form,data=data,blogComment=blog_comment,format_blog=format_blog,message=message,title=title,comments=form,blogs=blogs,id=id,del_comment=del_comment)

#profile picture

@main.route("/profile/<uname>")
def profile(uname):
    user=Users.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html",user=user)

@main.route("/profile/<uname>/update",methods=['GET','POST'])
def update_profile(uname):
    user=Users.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    form =UpdateProfile()
    if form.validate_on_submit():
        user.about=form.about.data
        user.occupation=form.occupation.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for(".profile",uname=user.username))

    return render_template("profile/update.html",form=form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
def update_pic(uname):
    user = Users.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile= path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))