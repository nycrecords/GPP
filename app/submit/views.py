from flask import render_template

from app.constants.boroughs import BOROUGH_LIST
from app.constants.community_board_districts import COMMUNITY_BOARD_DISTRICT_LIST
from app.constants.languages import LANGUAGE_LIST
from app.constants.report_types import REPORT_TYPE_LIST
from app.constants.school_districts import SCHOOL_DISTRICT_LIST
from app.constants.subjects import SUBJECTS_LIST
from app.submit import submit_views
from app.submit.forms import SubmitForm


@submit_views.route('/', methods=['GET', 'POST'])
def submit():
    submit_form = SubmitForm()
    submit_form.report_type.choices = [(report_type, report_type) for report_type in REPORT_TYPE_LIST]

    return render_template('submit.html',
                           form=submit_form,
                           subjects=SUBJECTS_LIST,
                           languages=LANGUAGE_LIST,
                           boroughs=BOROUGH_LIST,
                           school_districts=SCHOOL_DISTRICT_LIST,
                           community_board_districts=COMMUNITY_BOARD_DISTRICT_LIST)
