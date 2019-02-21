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


class SubmitForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=10, max=150)])
    subtitle = StringField('Sub-Title', validators=[Optional(), Length(min=0, max=150)])
    agency = SelectField('Agency', choices=[], validators=[DataRequired()])
    additional_creators = StringField('Additional Creator(s)', validators=[Optional(), Length(min=0, max=150)])
    subjects = SelectMultipleField('Subject(s)', choices=[], validators=[DataRequired()])  # TODO (gzhou): Add custom validator for max of three subjects
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=100, max=200)])
    date_published = DateField('Date Published', validators=[DataRequired()])
    report_type = SelectField('Report Type', choices=[], validators=[DataRequired()])
    fiscal_year = IntegerField('Associated Year - Fiscal', validators=[Optional(), Length(max=4)])  # TODO (gzhou): One of fiscal or calendar is required
    calendar_year = IntegerField('Associated Year - Calendar', validators=[Optional()])
    borough = SelectMultipleField('Associated Borough(s)', choices=[], validators=[Optional()])
    school_district = SelectMultipleField('Associated School District(s)', choices=[], validators=[Optional()])
    place_other = StringField('Associated Place (Other)', validators=[Optional(), Length(min=0, max=150)])
    submit_field = SubmitField('Submit Publication')
