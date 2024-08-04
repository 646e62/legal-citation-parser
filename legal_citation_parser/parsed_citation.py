# parsed_citation.py

class ParsedCitation:
    def __init__(self, uid, style_of_cause, atomic_citation, citation_type, 
                 official_reporter_citation, year, court, decision_number, 
                 jurisdiction, court_name, court_level, long_url, 
                 url_verified, short_url, language, docket_number, 
                 decision_date, keywords, categories, cited_cases, citing_cases, error):
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
        return f"<ParsedCitation: {self.style_of_cause} ({self.year})>"
    
    def __str__(self):
        return f"{self.style_of_cause} ({self.year})"
    
    # Add a method to return all the citation information in a dictionary format
    def full(self):
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
    