from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class ZipForm(FlaskForm):
    body = StringField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField('Submit')