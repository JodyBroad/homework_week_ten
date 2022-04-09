from flask import Flask, render_template, url_for

flask_blog_app = Flask(__name__)


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


if __name__ == "__main__":
    flask_blog_app.run(debug=True, port=4002)
