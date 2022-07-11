from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(3,15, message='Name must be between 3 and 15 characters.')])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(15), EqualTo('confirm', message="Passwords do not match.")])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Register')