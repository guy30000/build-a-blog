from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:beproductive@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):#needed that all to creat database and ability to enter 

    id = db.Column(db.Integer, primary_key=True)
    blg_title = db.Column(db.String(120))
    blg_body = db.Column(db.String(120)) #i dont know the max
    ##Part of blogz   keep off until ready
    #owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, blg_title, blg_body):
        self.blg_title = blg_title
        self.blg_body = blg_body
        ##Part of blogz  keep off until ready
        #self.owner = owner



@app.route('/blog', methods=['POST', 'GET'])
def index():
    
    blog = Blog.query.all()
    #bloglink_id = request.form['bloglink']
    bloglink_id = request.form['bloglink']
    #print(bloglink_id)
    #bloglink = Blog.query.get(bloglink_id)
    #user = Blog.query.get(id).first()
    print(blog)


    

    return render_template('blog.html',title="Build a Blog", blog=blog)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():

    if request.method == 'POST':
        blg_title = request.form['blg_title']
        blg_body = request.form['blg_body']
        if not blg_body or not blg_title:
            blg_fail =  "You need to fill out both things, guy."
            return render_template('newpost.html', blg_fail=blg_fail, blg_title=blg_title, blg_body=blg_body) 
        #Part of Blogz. Delete this next line when done with it
        #owner_id = ("?") #may als need to remove this v
        new_entry = Blog(blg_title, blg_body)#, owner_id)
        db.session.add(new_entry)
        db.session.commit()
        return render_template('blog_entry.html', blog=new_entry)

    return render_template('newpost.html')

#####THis isnt working yet V
@app.route('/blog_entry', methods=['POST', 'GET'])
def blog_entry(self, id):
    #blog = Blog.get_by_id(int(id))
    #tmplt = jinja.get_template('blog_entry.html')
    #response = tmplt.render(blog=blog)

    #blog = Blog.query.all()
    #blog_id = request.form['{{blog.id}}']
    #blog = Blog.query.filter_by(blog_id=blog_id).all()
  
    return render_template('blog_entry.html' + blog.id, blog=blog)

##############################################
####################### For Blogz
###User stuff
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    #check out this part, refering to Blog Keep off and edit when ready
    #tasks = db.relationship('Blog', backref='owner')

    def __init__(self, email, password):
        self.email = email
        self.password = password

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session['email'] = email
            flash("Logged in")
            return redirect('/')
        else:
            flash('User password incorrect, or user does not exist', 'error')

    return render_template('login.html')

### End User stuff
##Register
@app.route('/signup', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']

        # TODO - validate user's data

        existing_user = User.query.filter_by(email=email).first()
        if not existing_user:
            new_user = User(email, password)
            db.session.add(new_user)
            db.session.commit()
            #session['email'] = email
            return redirect('/')
        else:
            # TODO - user better response messaging
            blg_fail = ("Email has already been registered")
            return render_template('signup.html', blg_fail=blg_fail)


    return render_template('signup.html')
##end register

if __name__ == '__main__':
    app.run()