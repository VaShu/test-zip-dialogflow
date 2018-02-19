from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import DataRequired


class ZipGForm(FlaskForm):
    country = SelectField("Select country", choices=[('USA', 'United State'), ('Ukraine', 'Ukraine')])
    postal_code = StringField("Enter zip code", validators=[DataRequired()])
    submit = SubmitField('Search')
