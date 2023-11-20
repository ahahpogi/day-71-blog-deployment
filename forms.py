from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Regexp
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegistrationForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    email = StringField(
        "Email",
        validators=[DataRequired(),Regexp('.+@.+', message='Invalid email address')]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Regexp('^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,}$',
                   message='Password must be at least 6 characters long and contain at least one number and one symbol.'
                   )
        ]
    )
    submit = SubmitField("Sign Me Up!")

# TODO: Create a LoginForm to login existing users
class LogInForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let Me In!")

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit_comment = SubmitField("Post comment")