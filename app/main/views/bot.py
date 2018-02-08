from flask import render_template
from app.main.forms import BotForm
from .. import main


@main.route('/bot', methods=['GET', 'POST'])
def bot():
    form = BotForm()
    return render_template('bot.html', form=form)
