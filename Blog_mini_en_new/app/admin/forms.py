# coding:utf-8
from flask.ext.wtf import Form
from wtforms import SelectField, StringField, TextAreaField, SubmitField, \
    PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..main.forms import CommentForm


class CommonForm(Form):
    types = SelectField(u'Blog classification', coerce=int, validators=[DataRequired()])
    source = SelectField(u'Blog source', coerce=int, validators=[DataRequired()])


class SubmitArticlesForm(CommonForm):
    title = StringField(u'Title', validators=[DataRequired(), Length(1, 64)])
    content = TextAreaField(u'Blog content', validators=[DataRequired()])
    summary = TextAreaField(u'Blog Digest', validators=[DataRequired()])


class ManageArticlesForm(CommonForm):
    pass


class DeleteArticleForm(Form):
    articleId = StringField(validators=[DataRequired()])


class DeleteArticlesForm(Form):
    articleIds = StringField(validators=[DataRequired()])


class DeleteCommentsForm(Form):
    commentIds = StringField(validators=[DataRequired()])


class AdminCommentForm(CommentForm):
    article = StringField(validators=[DataRequired()])


class AddArticleTypeForm(Form):
    name = StringField(u'Classification name', validators=[DataRequired(), Length(1, 64)])
    introduction = TextAreaField(u'Classification introduction')
    setting_hide = SelectField(u'attribute', coerce=int, validators=[DataRequired()])
    menus = SelectField(u'Subordinate navigation', coerce=int, validators=[DataRequired()])
# You must add coerce=int, or the SelectFile validate function only validate the int data


class EditArticleTypeForm(AddArticleTypeForm):
    articleType_id = StringField(validators=[DataRequired()])


class AddArticleTypeNavForm(Form):
    name = StringField(u'Navigation name', validators=[DataRequired(), Length(1, 64)])


class EditArticleNavTypeForm(AddArticleTypeNavForm):
    nav_id = StringField(validators=[DataRequired()])


class SortArticleNavTypeForm(AddArticleTypeNavForm):
    order = StringField(u'Serial number', validators=[DataRequired()])


class CustomBlogInfoForm(Form):
    title = StringField(u'Blog title', validators=[DataRequired()])
    signature = TextAreaField(u'Personalized signature', validators=[DataRequired()])
    navbar = SelectField(u'Navigation style', coerce=int, validators=[DataRequired()])


class AddBlogPluginForm(Form):
    title = StringField(u'Plug-in name', validators=[DataRequired()])
    note = TextAreaField(u'Remarks')
    content = TextAreaField(u'content', validators=[DataRequired()])


class ChangePasswordForm(Form):
    old_password = PasswordField(u'Original password', validators=[DataRequired()])
    password = PasswordField(u'New password', validators=[
        DataRequired(), EqualTo('password2', message=u'Two inconsistent passwords！')])
    password2 = PasswordField(u'Confirm new password', validators=[DataRequired()])


class EditUserInfoForm(Form):
    username = StringField(u'nickname', validators=[DataRequired()])
    email = StringField(u'E-mail', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'Password confirmation', validators=[DataRequired()])
