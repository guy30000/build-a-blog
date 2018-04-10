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
        if not blg_body or not blg_title:
            blg_fail =  "You need to fill out both things, guy."
            return render_template('blog.html', blg_fail=blg_fail, blg_title=blg_title, blg_body=blg_body) 
        new_entry = Blog(blg_title, blg_body )
        db.session.add(new_entry)
        db.session.commit()
        return render_template('blog_entry.html', blog=new_entry)

    return render_template('blog.html')
#####THis isnt working yet V
@app.route('/blog_entry', methods=['POST', 'GET'])
def blog_entry(self, id):
    blog = Blog.get_by_id(int(id))
    tmplt = jinja.get_template('blog_entry.html')
    response = tmplt.render(blog=blog)
    self.response.write(response)
    blog = Blog.query.all()
    blog_id = request.form['{{blog.id}}']
    blog = Blog.query.filter_by(blog_id=blog_id).all()
  
    return render_template('blog_entry.html' + blog.id, blog=blog)






if __name__ == '__main__':
    app.run()