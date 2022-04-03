from flask import Flask, Response, request, url_for

app = Flask(__name__)


# these three routes are get requests
@app.route('/')
def welcome_to_flask():
    return "Welcome to Flask!"


@app.route('/hello')
def hello_from_flask():
    return "Hello from Flask!"


@app.route('/bye')
def bye_from_flask():
    return "Goodbye from Flask!"


@app.route('/post/text', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data: " + data_sent, mimetype='text/plain')


@app.route('/get/text')
def get_text():
    return Response("Hello from a RESPONSE object", mimetype='text/plain')


# url_for() method - slides
@app.route('/index/<name>/<int:age>')
def index(name, age):
    url = url_for('get_text')
    return """
<html>
<head>
    <title>Sample - Flask routes</title>
</head>
<body>
    <h1>Name page</h1>
    <p>Hello {}!</p>
    <p>You are {} years(s) old.</p>
    <hr>
    <a href="{}">Welcome</a>
</body>
</html>
""".format(name, age, url)


# url_for() method - practice
@app.route("/about/<name>/<location>")
def about(name, location):
    url = url_for('get_text')
    return """
<html>
<head>
    <title>About Page</title>
</head>
<body>
    <h1>About Us</h1>
    <p>Welcome to our About Page {}.</p>
    <p>Your location is: {}.</p>
    <hr>
    <a href="Find Us">Find Us</a>
</body>
</html>
""".format(name, location, url)


# Dynamic routes
# the route variable word is a string by default
# equivalent to @app.route('/dynamic/<string:word>')
@app.route('/dynamic/<word>')
def home(word):
    return word


# this route variable is an int type called number
@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = "Your number squared is" + " " + str(squared)
    return line


# Activity from slides
@app.route('/hello-you/<name>')
def hello_name(name):
    line = "Hello " + name
    return line


# Activity from slides
@app.route('/hello-page/<name>')
def say_hello_page(name):
    return """
    <html>
    <head>
        <title>Sample - Flask routes</title>
    </head>
    <body>
        <h1>Name page</h1>
        <p>Hello {}!</p>
    </body>
    </html>
""".format(name)


# Additional dynamic routes
@app.route('/cube/<int:number>')
def cube(number):
    cubed = number ** 3
    line = "Your number cubed is" + " " + str(cubed)
    return line


@app.route('/modulus/<int:number>')
def modulus(number):
    remainder = number % 2
    if remainder == 0:
        line = "Your number is even"
    else:
        line = "Your number is odd"
    return line


# use a different port reference for homework, e.g. 4001
# if this script is invoked directly (rather than being imported), run the flask app
if __name__ == "__main__":
    app.run(debug=True, port=4000)
