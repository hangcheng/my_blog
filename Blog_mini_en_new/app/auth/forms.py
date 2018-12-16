# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    email = StringField(u'E-mail', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField(u'Password', validators=[DataRequired()])
