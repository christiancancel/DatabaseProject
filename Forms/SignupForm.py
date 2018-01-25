from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    district = StringField('District', validators=[DataRequired()])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    user_type = RadioField('Account Type', validators=[DataRequired()],
                           choices=[('pin', 'Customer'), ('supplier', 'Supplier')], default='pin')
    submit = SubmitField('Sign Up')
