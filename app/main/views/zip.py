from flask import render_template, request
from app.main.forms import ZipForm, ZipGForm
from app.models import Zip
from .. import main
import requests as rq

GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

@main.route('/zip', methods=['GET', 'POST'])
def zip():
    form = ZipForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            current_zip = form.postal_code.data
            zip = Zip.query.filter_by(postal_code=current_zip).first()
            if zip is not None:
                latitude = zip.latitude
                longitude = zip.longitude
                return render_template('point.html', form=form, latitude=latitude, longitude=longitude)
            else:
                latitude = 0
                longitude = 0
                return render_template('point.html', form=form, latitude=latitude, longitude=longitude)

    else:
        return render_template("zip.html", form=form)

@main.route('/zipg', methods=['GET', 'POST'])
def zipg():
    form = ZipGForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            current_zip = form.postal_code.data
            country = form.country.data

            params = {
                'address': current_zip + ',' + country,
                'sensor': 'false',
                # 'region': 'uk'
            }

            # Do the request and get the response data
            req = rq.get(GOOGLE_MAPS_API_URL, params=params)
            res = req.json()

            if res is not None:
                # Use the first result
                result = res['results'][0]
                latitude = result['geometry']['location']['lat']
                longitude = result['geometry']['location']['lng']
                return render_template('point.html', form=form, latitude=latitude, longitude=longitude)
            else:
                latitude = 0
                longitude = 0
                return render_template('point.html', form=form, latitude=latitude, longitude=longitude)

    else:
        return render_template("zip.html", form=form)
