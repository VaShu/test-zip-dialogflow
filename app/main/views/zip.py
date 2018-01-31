from flask import render_template
from app.main.forms import ZipForm
from .. import main


@main.route('/zip/frame', methods=['GET', 'POST'])
def zip_frame():
    form = ZipForm()
    # resp = make_response(redirect(url_for('.index')))
    # return resp
    return render_template('zip.html', form=form)


@main.route('/zip/api', methods=['GET', 'POST'])
def zip_api():
    form = ZipForm()
    # resp = make_response(redirect(url_for('.index')))
    # return resp
    return render_template('zip.html', form=form)

