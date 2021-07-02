from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'John',
        'title': 'Blog Post 1',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean posuere velit a porta viverra. Curabitur id mauris ante. Fusce dapibus ante quis elit porttitor, vitae venenatis nisl tincidunt.',
        'date': '6/24/2021'
    },
    {
        'author': 'Cherry',
        'title': 'Blog Post 2',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean posuere velit a porta viverra. Curabitur id mauris ante. Fusce dapibus ante quis elit porttitor, vitae venenatis nisl tincidunt.',
        'date': '6/24/2021'
    }
]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about_page():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')       
    return render_template('login.html', title='Login', form=form)
