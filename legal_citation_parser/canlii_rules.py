# canlii_rules.py

import re
from .canlii_constants import COURT_CODES, COURT_CODE_MAP
from .utils import Utility, CanLIIAPI

class CanLIICitationParser:
    def __init__(
        self,
        citation: str,
        language="en",
        metadata=False,
        cited=False,
        citing=False,
        verify_url=False,
    ) -> None:
        self.citation = citation
        self.language = language
        self.metadata = metadata
        self.cited = cited
        self.citing = citing
        self.verify_url = verify_url
        self.alert_log = []
        self.diagnostic_log = []

    def check_court_code(self, year: str, court_code: str, uid: str) -> str:
        for court in COURT_CODE_MAP:
            if court_code == court[0]:
                database_id = court[1]
                break
        else:
            database_id = None

        # Account for changes in court codes over time
        if court_code == "qc cm" and int(year) >= 1983 and uid != "1983canlii2659":
            database_id = "qccmq"
        elif court_code == "qc cm" and int(year) <= 1983:
            database_id = "qccm"
        
        # Account for a court code used by two different courts
        elif court_code == "ca cb":
            if self.language == "en":
                database_id = "cbc"
            else:
                database_id = "cacp"

        return database_id

    def identify_court(self, database_id: str) -> tuple:
        if database_id:
            court_level = COURT_CODES[database_id]["court_type"]
            jurisdiction = COURT_CODES[database_id]["jurisdiction"]

            if jurisdiction == "qc":
                self.language = "fr"

            court_name = COURT_CODES[database_id]["name"][self.language]
        else:
            court_level = None
            jurisdiction = None
            court_name = None

        return court_level, jurisdiction, court_name

    def generate_uid(self, year, court_level, decision_number, citation_type):
        if citation_type == "canlii":
            uid = f"{year}canlii{decision_number}"
        else:
            uid = f"{year}{court_level}{decision_number}"
        return uid

    def search_right_to_left(self, pattern, text):
        matches = re.findall(pattern, text)
        if matches:
            last_match = matches[-1]
            last_pos = text.rfind(last_match)
            return last_pos, last_match
        return None

    def detect_official_reporter(self, citation):
        OFFICIAL_REPORTER_LIST = ["SCR", "RCS", "CF", "FC", "CMAR", "CACM", "Ex CR"]
        for reporter in OFFICIAL_REPORTER_LIST:
            if reporter in citation[1]:
                official_reporter_citation = citation[-1]
                citation = citation[0]
                return official_reporter_citation, citation
        official_reporter_citation = None
        return official_reporter_citation, citation

    def verify_citation_year(self, citation):
        pattern = r", \d{4} "
        year_match = self.search_right_to_left(pattern, citation)
        if year_match is None:
            year = None
        else:
            year = year_match[1].replace(", ", "").strip()
        return year

    def citation_metadata(self, year, citation):
        if citation and " CanLII " not in citation:
            citation_type = "neutral"
            court_code = citation.split(" ")[1].lower()
        elif citation and " CanLII " in citation:
            citation_type = "canlii"
            court_code = re.search(r"\(([^)]+)\)", citation).group(1).lower()
        else:
            citation_type = None
            court_code = None

        if citation and ", " in citation:
            citation_components = citation.split(", ")
            official_reporter_citation, citation = self.detect_official_reporter(
                citation_components
            )
        else:
            official_reporter_citation = None

        if citation:
            try:
                decision_number = citation.split(" ")[2]
            except (IndexError, AttributeError):
                decision_number = None

        if court_code and decision_number and citation_type:
            uid = self.generate_uid(year, court_code, decision_number, citation_type)
            uid = uid.replace(",", "")
            database_id = self.check_court_code(year, court_code, uid)
            court_level, jurisdiction, court_name = self.identify_court(database_id)
        else:
            uid = None
            court_level = None
            jurisdiction = None
            court_name = None
            decision_number = None

        return (
            citation_type,
            court_code,
            official_reporter_citation,
            court_level,
            jurisdiction,
            court_name,
            uid,
            decision_number,
            citation,
        )

    def separate_citation_elements(self, citation):
        try:
            citation = citation.replace(" (CanLII)", "")
            split_citation = re.split(r"(, \d{4} )", citation)
            style_of_cause = split_citation[0].replace(".", "")
            citation = split_citation[1].replace(", ", "") + split_citation[2]
        except IndexError:
            style_of_cause = None
            citation = None

        return style_of_cause, citation

    def fetch_api_data(self, uid, database_id):
        api_data = {}
        if self.metadata:
            api_metadata = CanLIIAPI.api_call(
                case_id=uid, database_id=database_id, decision_metadata=True
            )
            api_data.update(api_metadata)
        if self.cited:
            api_cited = CanLIIAPI.api_call(
                case_id=uid, database_id=database_id, cases_cited=True
            )
            api_data.update(api_cited)
        if self.citing:
            api_citing = CanLIIAPI.api_call(
                case_id=uid, database_id=database_id, cases_citing=True
            )
            api_data.update(api_citing)
        return api_data

    def parse(self):
        year = self.verify_citation_year(self.citation)
        style_of_cause, citation = self.separate_citation_elements(self.citation)

        (
            citation_type,
            court_code,
            official_reporter_citation,
            court_level,
            jurisdiction,
            court_name,
            uid,
            decision_number,
            atomic_citation,
        ) = self.citation_metadata(year, citation)

        if year and court_code and uid:
            database_id = self.check_court_code(year, court_code, uid)
        else:
            database_id = None

        if year and self.language and jurisdiction and database_id and year and uid:
            long_url = f"https://www.canlii.org/{self.language}/{jurisdiction}/{database_id}/doc/{year}/{uid}/{uid}.html"
        else:
            long_url = None

        citation_info = Citation(
            uid=uid,
            style_of_cause=style_of_cause,
            atomic_citation=atomic_citation,
            citation_type=citation_type,
            official_reporter_citation=official_reporter_citation,
            year=year,
            court=database_id,
            decision_number=decision_number,
            jurisdiction=jurisdiction,
            court_name=court_name,
            court_level=court_level,
            long_url=long_url,
            url_verified=False,
            short_url=None,
            language=self.language,
            docket_number=None,
            decision_date=None,
            keywords=[],
            categories=[],
            cited_cases=[],
            citing_cases=[],
            error=None,
        )

        if self.verify_url:
            citation_info.url_verified = Utility.check_url(long_url) is not None

        api_data = self.fetch_api_data(uid, database_id)
        for key, value in api_data.items():
            setattr(citation_info, key, value)

        return citation_info

# parsed_citation.py

class Citation:
    def __init__(self, uid, style_of_cause, atomic_citation, citation_type, 
                 official_reporter_citation, year, court, decision_number, 
                 jurisdiction, court_name, court_level, long_url, 
                 url_verified, short_url, language, docket_number, 
                 decision_date, keywords, categories, cited_cases, citing_cases, error):
        
        cited_cases = cited_cases["citedCases"] if cited_cases else []
        citing_cases = citing_cases["citingCases"] if citing_cases else []
        
        self.uid = uid
        self.style_of_cause = style_of_cause
        self.atomic_citation = atomic_citation
        self.citation_type = citation_type
        self.official_reporter_citation = official_reporter_citation
        self.year = year
        self.court = court
        self.decision_number = decision_number
        self.jurisdiction = jurisdiction
        self.court_name = court_name
        self.court_level = court_level
        self.long_url = long_url
        self.url_verified = url_verified
        self.short_url = short_url
        self.language = language
        self.docket_number = docket_number
        self.decision_date = decision_date
        self.keywords = keywords
        self.categories = categories
        self.cited_cases = cited_cases
        self.citing_cases = citing_cases
        self.error = error

    def __repr__(self):
        return f"<Citation: {self.style_of_cause}, {self.atomic_citation}>"
    
    def __str__(self):
        return f"{self.style_of_cause} ({self.year})"
    
    # Add a method to return all the citation information in a dictionary format
    def parse(self):
        """
        Returns all the citation information in a dictionary format.

        Returns:
            dict: A dictionary containing all the citation information
        """
        return {
            "uid": self.uid,
            "style_of_cause": self.style_of_cause,
            "atomic_citation": self.atomic_citation,
            "citation_type": self.citation_type,
            "official_reporter_citation": self.official_reporter_citation,
            "year": self.year,
            "court": self.court,
            "decision_number": self.decision_number,
            "jurisdiction": self.jurisdiction,
            "court_name": self.court_name,
            "court_level": self.court_level,
            "long_url": self.long_url,
            "url_verified": self.url_verified,
            "short_url": self.short_url,
            "language": self.language,
            "docket_number": self.docket_number,
            "decision_date": self.decision_date,
            "keywords": self.keywords,
            "categories": self.categories,
            "cited_cases": self.cited_cases,
            "citing_cases": self.citing_cases,
            "error": self.error
        }
    