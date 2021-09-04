from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, RadioField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User, Post
from flaskblog import db


class RegistrationForm(FlaskForm):
    voter_id = StringField('Voter ID',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    dob= DateField('DOB', validators=[DataRequired()], format="%d-%m-%Y")
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_voterID(self, voter_id):
        user = User.query.filter_by(voter_id=voter_id.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    voter_id = StringField('Voter ID',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    dob= DateField('DOB', validators=[DataRequired()], format="%d-%m-%Y")
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    c1 = StringField('Candidate-1', validators=[DataRequired()])
    c2 = StringField('Candidate-2', validators=[DataRequired()])
    c3 = StringField('Candidate-3', validators=[DataRequired()])
    c4 = StringField('Candidate-4', validators=[DataRequired()])
    c5 = StringField('Candidate-5', validators=[DataRequired()])
    submit = SubmitField('Create Election')

class Vote_Form(FlaskForm):
    v= RadioField('Select Candidate', choices=[('1', 'a'), ('2', 'b'), ('3', 'c'), ('4','d'), ('5', 'e')], validators=[DataRequired()])
    submit = SubmitField('Cast Vote')