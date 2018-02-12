from flask import render_template, request
from app.main.forms import ZipForm
from app.models import Zip
from .. import main


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
