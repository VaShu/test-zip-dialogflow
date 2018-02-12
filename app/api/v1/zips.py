from flask import jsonify
from . import api
from app.models import Zip


@api.route('/zips/<string:postal_code>')
def get_zip(postal_code):
    zip = Zip.query.filter_by(postal_code=postal_code).first()
    if zip is not None:
        return jsonify(zip.to_json())
    else:
        msg = {"msg": " zip code not found"}
        return jsonify(msg)
