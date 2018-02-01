from flask import jsonify
from . import api
from app.models import Zip


@api.route('/zips/<string:postal_code>')
def get_zip(postal_code):
    zip = Zip.query.get_or_404(postal_code)
    return jsonify(zip.to_json())
