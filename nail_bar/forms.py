from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email


class AppointmentForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('E-mail Address', validators=[DataRequired(), Email()])
    phone = StringField('Contact Telephone Number', validators=[DataRequired()])
    time = StringField('Appointment date and time requested', validators=[DataRequired()])
    service = StringField('Service requested', validators=[DataRequired()])
    # dropdown - should we hard code a list of the services? can we pull it from the dictionary, or can we create dynamic list somehow?
    # service = SelectField('Service requested', choices=[(service.service)]([DataRequired()])
    submit = SubmitField('Submit Appointment Request')


class ContactForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('E-mail address')
    message = StringField('Your message')
    submit = SubmitField('Submit contact form')
