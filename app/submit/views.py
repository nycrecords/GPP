from flask import render_template

from app.submit import submit_views
from app.submit.forms import SubmitForm


@submit_views.route('/', methods=['GET', 'POST'])
def submit():
    return render_template('submit.html', form=SubmitForm())
