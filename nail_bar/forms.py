from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class AppointmentForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('E-mail address')
    phone = StringField('Contact Telephone Number')


class ContactForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('E-mail address')
    message = StringField('Your message')
    submit = SubmitField('Submit contact form')
