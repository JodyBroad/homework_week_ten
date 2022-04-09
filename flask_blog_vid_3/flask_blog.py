from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

flask_blog_app = Flask(__name__)

flask_blog_app.config['SECRET_KEY'] = 'e0b3b359461fab01e70f38bbee9045e9'
# import os
# flask_blog_app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# in reality we would be calling this info from a database
posts = [
    {
        'author': 'Jody Broad',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '01/04/2022'
    },
    {
        'author': 'Alice Caffyn',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '02/04/2022'
    }
]

# can use more than one decorator at a time, so if you typed either '/' or '/home' you get the same stuff returned
@flask_blog_app.route('/')
@flask_blog_app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@flask_blog_app.route('/about')
def about():
    return render_template('about.html', title='About')

@flask_blog_app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@flask_blog_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # fake login for now as we don't have database connection yet
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    flask_blog_app.run(debug=True, port=4002)
