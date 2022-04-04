from flask import Flask, Response, request, url_for, render_template

# instantiate the Flask application object
nail_bar_app = Flask(__name__)

# in reality, we would be calling this info from a database, dictionary of services to use for price_list
services = [
    {
        'service': 'French Manicure',
        'price': '£30',
        'nail_artist': 'Jody Broad',
        'time_required': '45 minutes'
    },
    {
        'service': 'Gel Polish',
        'price': '£45',
        'nail_artist': 'Alice Caffyn',
        'time_required': '1 hour'
    },
    {
        'service': 'Soak and remove existing gel polish',
        'price': '£5',
        'nail_artist': 'Jody Broad',
        'time_required': '15 minutes'
    },
    {
        'service': 'Acrylic nails - full set',
        'price': '£85',
        'nail_artist': 'Alice Caffyn',
        'time_required': ' 1 hour 45 minutes'
    },
    {
        'service': 'Acrylic nails - infills',
        'price': '£35',
        'nail_artist': 'Alice Caffyn',
        'time_required': '25 minutes'
    }


]

# can use more than one decorator at a time, so if you typed either '/' or '/home' you get the same stuff returned


@nail_bar_app.route('/')
@nail_bar_app.route('/home')
def home():
    return render_template('home.html')


@nail_bar_app.route('/about')
def about():
    return render_template('about.html', title='About')


@nail_bar_app.route('/price_list')
def price_list():
    return render_template('price_list.html', title='Price List', services=services)


@nail_bar_app.route('/cube/<int:number>')
def cube(number):
    cubed = number ** 3
    line_cube = "Your number cubed is" + " " + str(cubed)
    return render_template('maths.html', line_cube=line_cube)


@nail_bar_app.route('/modulus/<int:number>')
def modulus(number):
    remainder = number % 2
    if remainder == 0:
        line_mod = "Your number is even"
    else:
        line_mod = "Your number is odd"
    return render_template('maths.html', line_mod=line_mod)


@nail_bar_app.route('/dynamic/<word>')
def home_redirect(word):
    destination = url_for('home')
    return render_template('redirect.html', destination=destination)


if __name__ == "__main__":
    nail_bar_app.run(debug=True, port=4003)
