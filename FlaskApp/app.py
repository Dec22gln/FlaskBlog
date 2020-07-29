from flask import Flask
from flask import  render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/hire-me')
def hireMe():
    return render_template('hire-me.html')

@app.route('/project-page')
def projectPage():
    return render_template('project-page.html')

@app.route('/projects-compact-grid')
def projects1():
    return render_template('projects-compact-grid.html')

@app.route('/projects-no-images')
def projects2():
    return render_template('projects-no-images.html')

@app.route('/projects-with-sidebar')
def projects3():
    return render_template('projects-with-sidebar.html')

@app.route('/projects-grid-cards')
def projects4():
    return render_template('projects-with-sidebar.html')

if __name__ == '__main__':
    app.run()
