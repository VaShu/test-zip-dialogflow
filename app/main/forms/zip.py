from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired


class ZipForm(FlaskForm):
    postal_code = StringField("Enter zip code", validators=[DataRequired()])
    submit = SubmitField('Search')