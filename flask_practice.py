# homework is to practice with Flask using the notes - have something to demonstrate during the tutor session

from flask import Flask, Response, request, url_for

# instantiate the Flask application object
flask_practice_app = Flask(__name__)

# set up a route and bind a function as its response
# route decorator plus url that someone is going to type in


@flask_practice_app.route('/')
def welcome_to_flask():
    return "Welcome to Flask!"


@flask_practice_app.route('/hello')
def hello_from_flask():
    return "Hello from Flask!"


@flask_practice_app.route('/bye')
def bye_from_flask():
    return "Goodbye from Flask!"


@flask_practice_app.route('/get/text')
def get_text():
    return Response("Hello from RESPONSE object!", mimetype='text/plain')


# need to use postman to test this one, as browser can only do get requests


@flask_practice_app.route('/somethingelse', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data: " + data_sent, mimetype='text/plain')


# the route variable word is a string by default
# equivalent to the @app.route('/dynamic/<string:word>')


@flask_practice_app.route('/dynamic/<word>')
def home(word):
    return word

# activity from slide


@flask_practice_app.route('/dynamic/name/<word>')
def dynamic_name(word):
    return Response("Hello " + word)


# this route variable is an int type called number


@flask_practice_app.route('/cube/<int:number>')
def cube(number):
    cubed = number ** 3
    line = "Your number cubed is " + str(cubed)
    return line

# return an HTML page


@flask_practice_app.route('/say_hello/<name>')
def say_hello_page(name):
    return """
<html>
<head>
    <title>Sample - Flask routes</title>
</head>
<body>
    <h1>Name page</h1>
    <p> Hello {}!</p>
</body>
</html>
""".format(name)


# url_for() method


@flask_practice_app.route('/get/moretext')
def practice_get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')


@flask_practice_app.route('/index/<name>/<int:age>')
def index(name, age):
    url = url_for('practice_get_text')
    return """
<html>
<head>
    <title>Sample - Flask routes</title>
</head>
<body>
    <h1>Name and age page</h1>
    <p> Hello {}!</p>
    <p>You are {} year(s) old</p>
    <hr>
    <a href="{}>Welcome</a>
</body>
</html>
""".format(name, age, url)


@flask_practice_app.route('/index/about/<name>/<favourite_colour>')
def about(name, favourite_colour):
    url = url_for('practice_get_text')
    return """
<html>
<head>
    <title>Sample - Flask routes</title>
</head>
<body>
    <h1>About us and your favourite colour</h1>
    <p> Hello {}!</p>
    <p> We are so glad you popped by today - this page was built by Jody and Alice
    <p> Your favourite colour is {}.</p>
    <hr>
    <a href="{}>Welcome</a>
</body>
</html>
""".format(name, favourite_colour, url)


# if this script is invoked directly (rather than being imported), run the flask app
# the main trick is super important for flask
if __name__ == "__main__":
    flask_practice_app.run(debug=True, port=4001)


# could also do app.run(debug=True, port=4000) this is important for the homework - can run different things on
# different ports
# run method is what brings it to life and makes it a callable web object
# debug=True will give us information if you get an error, so we will generally use this
