from flask_wtf import FlaskForm
from wtforms import SubmitField


class PointForm(FlaskForm):
    submit = SubmitField('Return')