from flask import url_for
from app import db


class Zip(db.Model):
    __tablename__ = 'postzip'

    id = db.Column(db.Integer, primary_key=True)
    postal_code = db.Column(db.String(64))
    latitude = db.Column(db.String(64))
    longitude = db.Column(db.String(64))

    def __init__(self, **kwargs):
        super(Zip, self).__init__(**kwargs)

    def to_json(self):
        json_zip = {
            'url':
                url_for('api.get_zip', postal_code=self.postal_code, _external=True),
            'postal_code':
                self.postal_code,
            'latitude':
                self.latitude,
            'longitude':
                self.longitude,
        }
        return json_zip

    def __repr__(self):
        return '<Postal Code %r>' % self.postal_code
