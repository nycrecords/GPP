from enum import Enum


class ReportTypeEnum(Enum):
    ADJUDICATIONS_DECISIONS = 'Adjudications / Decisions'
    AUDIT_REPORT = 'Audit Report'
    BROCHURES = 'Brochures'
    BUDGET_FINANCE = 'Budget / Finance'
    BULLETINS = 'Bulletins'
    CALENDARS = 'Calendars'
    DATA_STATISTICS = 'Data / Statistics'
    DIRECTIVES = 'Directives'
    ENVIRONMENTAL_IMPACT_STATEMENTS_DRAFT = 'Environmental Impact Statements - Draft'
    ENVIRONMENTAL_IMPACT_STATEMENTS_FINAL = 'Environmental Impact Statements - Final'
    EXECUTIVE_ORDERS = 'Executive Orders'
    GUIDES = 'Guides'
    LAWS_LEGISLATION = 'Laws / Legislation'
    MANUALS_DIRECTORIES = 'Manuals / Directories'
    MINUTES = 'Minutes'
    NEWSLETTERS_OTHER_SERIAL_PUBLICATIONS = 'Newsletters / Other Serial Publications'
    OTHER = 'Other'
    PLANS = 'Plans'
    PRESS_RELEASES = 'Press Releases'
    PROCEEDINGS = 'Proceedings'
    REPORTS_ANNUAL = 'Reports - Annual'
    REPORTS_BIENNIAL = 'Reports - Biennial'
    REPORTS_MONTHLY = 'Reports - Monthly'
    REPORTS_WEEKLY = 'Reports - Weekly'
    REPORTS_OTHER_CONSULTANT_STAFF = 'Reports - Other (Consultant/Staff)'
    STUDIES = 'Studies'


REPORT_TYPE_LIST = [r.value for r in ReportTypeEnum]
