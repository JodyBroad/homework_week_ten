from flask import Flask, Response, request, url_for, render_template

# instantiate the Flask application object
nail_bar_app = Flask(__name__)

# in reality we would be calling this info from a database
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


if __name__ == "__main__":
    nail_bar_app.run(debug=True, port=4003)
