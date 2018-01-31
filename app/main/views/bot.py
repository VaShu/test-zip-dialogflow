from flask import render_template
from app.main.forms import BotForm
from .. import main


@main.route('/bot/frame', methods=['GET', 'POST'])
def bot_frame():
    form = BotForm()
    # resp = make_response(redirect(url_for('.index')))
    # return resp
    return render_template('bot.html', form=form)


@main.route('/bot/api', methods=['GET', 'POST'])
def bot_api():
    form = BotForm()
    # resp = make_response(redirect(url_for('.index')))
    # return resp
    return render_template('bot.html', form=form)
