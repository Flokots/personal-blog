
from wtforms import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired



class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you.', validators=[DataRequired()])
  submit = SubmitField('Submit')


class AddBlog(FlaskForm):
  name = StringField('Blog Name', validators=[DataRequired()])
  content = TextAreaField('Blog content')
  submit = SubmitField('Submit')


class UpdateBlog(FlaskForm):
  name = StringField('Blog Name', validators=[DataRequired()])
  content = TextAreaField('Blog content')
  submit = SubmitField('Submit')

class CommentForm(FlaskForm):
  name = StringField('Comment', validators=[DataRequired()])
  submit = SubmitField('Submit')

  
