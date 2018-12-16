#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Optional


class CommentForm(Form):
    name = StringField(u'Nickname', validators=[DataRequired()])
    email = StringField(u'E-mail', validators=[DataRequired(), Length(1, 64),
                                            Email()])
    content = TextAreaField(u'Content', validators=[DataRequired(), Length(1, 1024)])
    follow = StringField(validators=[DataRequired()])
