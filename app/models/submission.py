from sqlalchemy.dialects.postgresql import ARRAY

from app import db
from app.constants.boroughs import BoroughEnum
from app.constants.community_board_districts import CommunityBoardDistrictEnum
from app.constants.report_types import ReportTypeEnum
from app.constants.school_districts import SchoolDistrictEnum


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    subtitles = db.Column(ARRAY(db.String(150)), nullable=True)
    # agency_ein = db.Column(db.String(4), db.ForeignKey('agency.ein'), nullable=False)
    additional_creators = db.Column(ARRAY(db.String(150)), nullable=True)
    subjects = db.Column(ARRAY(db.String), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    date_published = db.Column(db.Date, nullable=False)
    report_type = db.Column(db.Enum(ReportTypeEnum), nullable=False)
    languages = db.Column(ARRAY(db.String()), nullable=False)
    fiscal_years = db.Column(ARRAY(db.SmallInteger()), nullable=True)
    calendar_years = db.Column(ARRAY(db.SmallInteger()), nullable=True)
    boroughs = db.Column(ARRAY(db.Enum(BoroughEnum)), nullable=True)
    school_districts = db.Column(ARRAY(db.Enum(SchoolDistrictEnum)), nullable=True)
    community_board_districts = db.Column(ARRAY(db.Enum(CommunityBoardDistrictEnum)), nullable=True)

    def __init__(self,
                 title,
                 # agency_ein,
                 subjects,
                 description,
                 date_published,
                 report_type,
                 languages,
                 subtitles=None,
                 additional_creators=None,
                 fiscal_years=None,
                 calendar_years=None,
                 boroughs=None,
                 school_districts=None,
                 community_board_districts=None):
        self.title = title
        # self.agency_ein = agency_ein
        self.subjects = subjects
        self.description = description
        self.date_published = date_published
        self.report_type = report_type
        self.languages = languages
        self.additional_creators = additional_creators
        self.fiscal_years = fiscal_years
        self.calendar_years = calendar_years
        self.boroughs = boroughs
        self.school_districts = school_districts
        self.community_board_districts = community_board_districts
        self.subtitles = subtitles
