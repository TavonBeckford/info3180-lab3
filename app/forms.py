from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, Email
from werkzeug.utils import secure_filename


class ContactForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(max=60)])
    email = EmailField('email', validators=[Email(), InputRequired(), Length(max=40)])
    subject = StringField('subject', validators=[InputRequired(), Length(max=40)])
    message = TextAreaField('message', validators=[InputRequired(), Length(max=150)])
