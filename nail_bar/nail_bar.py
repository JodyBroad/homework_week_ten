from flask import Flask, Response, request, url_for, render_template

# instantiate the Flask application object
from homework_week_ten.nail_bar.forms import ContactForm, AppointmentForm

nail_bar_app = Flask(__name__)

nail_bar_app.config['SECRET_KEY'] = 'e0b3b359461fab01e70f38bbee9045e9'

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


# uses the secret maths template
@nail_bar_app.route('/cube/<int:number>')
def cube(number):
    cubed = number ** 3
    line_cube = "Your number cubed is" + " " + str(cubed)
    return render_template('maths.html', line_cube=line_cube)


# uses the secret maths template
@nail_bar_app.route('/modulus/<int:number>')
def modulus(number):
    remainder = number % 2
    if remainder == 0:
        line_mod = "Your number is even"
    else:
        line_mod = "Your number is odd"
    return render_template('maths.html', line_mod=line_mod)


# will redirect if they type in something random using url_for()
@nail_bar_app.route('/dynamic/<word>')
def home_redirect(word):
    destination = url_for('home')
    return render_template('redirect.html', destination=destination)


@nail_bar_app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    error = ""
    form = AppointmentForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        phone = form.phone.data
        time = form.time.data
        service = form.service.data

        if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or len(phone) == 0 \
                or len(time) == 0 or len(service) == 0:
            error = "Please fill out all fields"
        else:
            return "Thank you, appointment request sent!"
    return render_template('appointment.html', title='Appointments', form=form, message=error)


# will post an appointment request - would do this using a form when we know how!
@nail_bar_app.route('/post/appointment', methods=['POST'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return render_template('appointment.html', data_sent=data_sent, mimetype='text/plain')


@nail_bar_app.route('/contact', methods=['GET', 'POST'])
def contact():
    error = ""
    form = ContactForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        message = form.message.data

        if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or '@' not in email or len(message) == 0:
            error = "Please supply all required fields"
        else:
            return 'Thank you for contacting us. We will respond to you shortly'
    return render_template('contact.html', title='Contact Us', form=form, message=error)


if __name__ == "__main__":
    nail_bar_app.run(debug=True, port=4003)
