from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required , Email, EqualTo
from ..models import Group
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Enter a valid Email address',validators = [Required(),Email()])
    name = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Password',validators=[Required(),EqualTo('password_confirm',message = 'Password must match')])
    password_confirm = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if Group.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if Group.query.filter_by(username=data_field.data).first():
            raise ValidationError('Username taken,try something else')


class LoginForm(FlaskForm):
    email = StringField('Your email address',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('LogIn')