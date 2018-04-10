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

    def __init__(self, blg_title, blg_body):
        self.blg_title = blg_title
        self.blg_body = blg_body


#class User(db.Model):

#    id = db.Column(db.Integer, primary_key=True)
#    email = db.Column(db.String(120), unique=True)
#    password = db.Column(db.String(120))

#    def __init__(self, email, password):
#        self.email = email
#        self.password = password


#@app.route('/login')
#def login():
#    return render_template('login.html')


#@app.route('/register')
#def register():
#    return render_template('register.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    #if request.method == 'POST':
        #task_name = request.form['task']
        #new_task = Task(task_name)
        #db.session.add(new_task)
        #db.session.commit()

    #tasks = Task.query.filter_by(completed=False).all()
    #completed_tasks = Task.query.filter_by(completed=True).all()
    #return render_template('blog.html',title="Build a Blog", tasks=tasks, completed_tasks=completed_tasks)
    blog = Blog.query.all()
   
    return render_template('homepage.html',title="Build a Blog", blog=blog)


@app.route('/blog', methods=['POST', 'GET'])
def blog():

    if request.method == 'POST':
        blg_title = request.form['blg_title']
        blg_body = request.form['blg_body']
        new_entry = Blog(blg_title, blg_body )
        db.session.add(new_entry)
        db.session.commit()
        return render_template('blog_entry.html', blog=new_entry)


#    return redirect('/')



    return render_template('blog.html')



#@app.route('/delete-task', methods=['POST'])
#def delete_task():




if __name__ == '__main__':
    app.run()