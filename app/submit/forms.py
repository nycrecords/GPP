from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms import IntegerField
from wtforms import SelectField
from wtforms import SelectMultipleField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Optional

from app.constants.boroughs import BOROUGH_LIST
from app.constants.community_board_districts import COMMUNITY_BOARD_DISTRICT_LIST
from app.constants.report_types import REPORT_TYPE_LIST
from app.constants.school_districts import SCHOOL_DISTRICT_LIST
from app.constants.subjects import SUBJECT_LIST


class SubmitForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=10, max=150)])
    subtitle = StringField('Sub-Title', validators=[Optional(), Length(min=0, max=150)])
    agency = SelectField('Agency', choices=[], validators=[DataRequired()])
    additional_creators = StringField('Additional Creator(s)', validators=[Optional(), Length(min=0, max=150)])
    subjects = SelectMultipleField('Subject(s)', choices=[], validators=[DataRequired()])  # TODO (gzhou): Add custom validator for max of three subjects
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=100, max=200)])
    date_published = DateField('Date Published', validators=[DataRequired()])
    report_type = SelectField('Report Type', choices=[], validators=[DataRequired()])
    fiscal_years = IntegerField('Associated Year - Fiscal', validators=[Optional(), Length(max=4)])  # TODO (gzhou): One of fiscal or calendar is required
    calendar_years = IntegerField('Associated Year - Calendar', validators=[Optional()])
    boroughs = SelectMultipleField('Associated Borough(s)', choices=[], validators=[Optional()])
    school_districts = SelectMultipleField('Associated School District(s)', choices=[], validators=[Optional()])
    community_board_districts = SelectMultipleField(
        'Associated Community Board District(s)', choices=[], validators=[Optional()])
    place_others = StringField('Associated Place (Other)', validators=[Optional(), Length(min=0, max=150)])
    submit_field = SubmitField('Submit Publication')

    def __init__(self):
        super(SubmitForm, self).__init__()
        self.subjects.choices = [(s, s) for s in SUBJECT_LIST]
        self.report_type.choices = [(r, r) for r in REPORT_TYPE_LIST]
        self.boroughs.choices = [(b, b) for b in BOROUGH_LIST]
        self.school_districts.choices = [(sd, sd) for sd in SCHOOL_DISTRICT_LIST]
        self.community_board_districts.choices = [(c, c) for c in COMMUNITY_BOARD_DISTRICT_LIST]
