from flask import Blueprint, render_template

#app = Blueprint('app', __name__)
app = Blueprint('frontend', __name__, template_folder='templates', static_folder='static', static_url_path='/frontend/static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/join')
def join():
    return render_template('join.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
