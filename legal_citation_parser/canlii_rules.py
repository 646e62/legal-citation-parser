"""
canlii_rules
Rule set for parsing CanLII citations and constructing CanLII URLs, as well as neutral citations.
"""

import re

from .canlii_constants import (
    COURT_CODES,
    COURT_CODE_MAP,
)

from .utils import canlii_api_call, check_url

def check_court_code(year, court_code, citation, citation_type, language="en"):
    """
    Court code fine-tuning function to ensure consistency in the court code format.
    """

    for court in COURT_CODE_MAP:
        if court_code == court[0]:
            database_id = court[1]
            break
    else:
        return None, None, None
    # Add error handling for court codes not in the map
    
            
    decision_number = citation.split(" ")[2]
    uid = generate_uid(year, court_code, decision_number, citation_type)

    # Duplicate court_code handling
    # Current limitations may be fine-tunable with CanLII API access
    # Corrects for SCC and SCC-l applications by defaulting to SCC
    if court_code == "scc" or database_id == "csc":
        database_id = "csc-scc"
    
    # Separates "qc cm" citations by year
    # The QCCMQ database took over "qc cm" after and including 1983, with one exception 
    # (1983canlii2659)
    elif court_code == "qc cm" and int(year) >= 1983 and uid != "1983canlii2659":
        database_id = "qccmq"
    elif court_code == "qc cm" and int(year) <= 1983:
        database_id = "qccm"

    # cbc/cacp - decide based on language
    # The "ca cb" court code is used for both the CBC and CACP databases. CBC is an English 
    # abbreviation for the Copyright Board of Canada, and CACP is the French abbreviation for
    # the Commissaire aux brevets
    elif court_code == "ca cb":
        if language == "en":
            database_id = "cbc"
        else:
            database_id = "cacp"

    return uid, decision_number, database_id

def generate_uid(year: str, court_level: str, decision_number: str, citation_type: str) -> str:
    """
    Generates a unique identifier (UID) for a CanLII case based on the year, court level, and
    decision number. The UID is used to construct the CanLII URL, as well as for API calls.

    Args:
        year (str): The year of the decision.
        court_level (str): The court level abbreviation.
        decision_number (str): The decision number.
        citation_type (str): The type of citation to generate.

    Returns:
        str: The generated unique identifier for the CanLII case.
    """

    citation = ""

    if citation_type == "canlii":
        citation = f"{year}canlii{decision_number}"
    else:
        citation = f"{year}{court_level}{decision_number}"

    return citation

def canlii_citation_parser(
    citation: str,
    language: str = "en",
    metadata: bool = False,
    cited: bool = False,
    citing: bool = False,
    verify_url: bool = False,
) -> dict:
    """
    Rules for parsing a CanLII citation string to extract metadata information.

    Args:
        citation (str): The CanLII citation string to parse.
        include_url (bool): A flag to determine whether to include the CanLII URL in the output.

    Returns:
        dict: A dictionary containing the parsed information, including the style of cause,
        citation, citation type (neutral or CanLII), year, court code, decision number,
        jurisdiction, court name, and court level. If `include_url` is True, the dictionary will
        also include the CanLII URL.
    """

    def search_right_to_left(pattern, text):
        """
        Single use function to search for a pattern in a string from right to left. Used for the 
        rare case (1% of 1% of cases on a recent test) where the style of cause contains a four-digit
        number followed by a comma and a space. This function solves this problem by effectively 
        reading the string backwards, searching for the last instance of the pattern.
        
        This subfunction can be moved to a utility module if it proves useful elsewhere.

        Args:
            pattern (str): The regex pattern to search for. r", \d{4} " in the canlii_citation_parser
                function.
            text (str): The text to search in.
        """
        
        matches = re.findall(pattern, text)
        
        if matches:
            # Return the last match found
            last_match = matches[-1]
            # To find the exact position of the last match:
            last_pos = text.rfind(last_match)
            return last_pos, last_match
        return None


    def generate_court_metadata(database_id, language):
        """
        DRY function to check the court database ID and return the court level, jurisdiction, and
        court name.
        """

        court_level = COURT_CODES[database_id]["court_type"]
        jurisdiction = COURT_CODES[database_id]["jurisdiction"]
    
        # Default to French for Quebec decisions for now
        if jurisdiction == "qc":
            language = "fr"
        
        court_name = COURT_CODES[database_id]["name"][language]

        return court_level, jurisdiction, court_name


    def detect_official_reporter(citation):
        """
        Single use function to detect and extract the official reporter citation from the atomic
        citation. This function is used to handle the rare case where the citation contains an
        official reporter citation in addition to the atomic citation.
        """
        OFFICIAL_REPORTER_LIST = [
            "SCR",
            "RCS",
            "CF",
            "FC",
        ]

        for reporter in OFFICIAL_REPORTER_LIST:
            if reporter in citation[1]:
                official_reporter_citation = citation[-1]
                citation = citation[0]
                return official_reporter_citation, citation
                
        official_reporter_citation = None

        return official_reporter_citation, citation


    def verify_citation_year(citation):
        """
        Absent a very unusually-named court case, the style of cause will always be separated from the
        rest of the citation by a comma, space, a four-digit year, and another space. This single use
        function captures the style of cause.
        """

        # Modified regex pattern to include checking for an alpha character after the year
        pattern = r", \d{4} "
        
        # Use the modified search function
        year_match = search_right_to_left(pattern, citation)
        
        if year_match is None:
            return "Error: citation string must contain a four-digit year followed by a space and an alpha character"
        else:
            # Extract the year and the character
            year = year_match[1].replace(", ", "").strip()
            return year


    citation = citation.replace(" (CanLII)", "")
    year = verify_citation_year(citation)
    split_citation = re.split(r"(, \d{4} )", citation)
    style_of_cause = split_citation[0].replace(".", "")
    citation = split_citation[1].replace(", ", "") + split_citation[2]

    # Determine the atomic citation type
    if citation and " CanLII " not in citation:
        citation_type = "neutral"
        court_code = citation.split(" ")[1].lower()
    elif citation and " CanLII " in citation:
        citation_type = "canlii"
        court_code = re.search(r"\(([^)]+)\)", citation).group(1).lower()
    else:
        return "Error: not a recognized CanLII citation format"

    # Construct the citation string
    try:
        if ", " in citation:
            citation = citation.split(", ")
            official_reporter_citation, citation = detect_official_reporter(citation)
        
        else:
            official_reporter_citation = None
    
    except IndexError:
        return "Error: citation must contain a court code and decision number"

    # Generate the unique identifier, decision number, and database ID
    uid, decision_number, database_id = check_court_code(year, court_code, citation, citation_type, language)
   
    # Return an error if the court code is not recognized
    if uid is None:
        return f"Error: court code {court_code} not recognized"
    else:
        uid = uid.replace(",", "")
        court_level, jurisdiction, court_name = generate_court_metadata(database_id, language)
    
    # Construct the long URL
    long_url = f"https://www.canlii.org/{language}/{jurisdiction}/{database_id}/doc/{year}/{uid}/{uid}.html"


    # Construct the citation information dictionary
    citation_info = {
        "uid": uid,
        "style_of_cause": style_of_cause,
        "atomic_citation": citation,
        "citation_type": citation_type,
        "official_reporter_citation": official_reporter_citation,
        "year": year,
        "court": database_id,
        "decision_number": decision_number,
        "jurisdiction": jurisdiction,
        "court_name": court_name,
        "court_level": court_level,
        "long_url": long_url,
    }

    # Kwargs

    ## Utility
    ### Long URL verification
    if verify_url:
        if check_url(long_url):
            print("URL is valid")
            pass
        else:
            # Check long_url, but with the opposite language ("fr" instead of "en" and vice versa)
            # This is a temporary solution to the language issue
            if language == "en":
                alt_language = "fr"
            else:
                alt_language = "en"
            alt_url = f"https://www.canlii.org/{alt_language}/{jurisdiction}/{database_id}/doc/{year}/{uid}/{uid}.html"
            if check_url(alt_url):
                citation_info["long_url"] = alt_url
                print("Alt URL is valid")
            else:
                citation_info["long_url"] = None


    ## API fine-tuning
    ### Metadata
    if metadata:
        api_info = canlii_api_call(uid, database_id, decision_metadata=True)
        citation_info.update(api_info)
    
    ### Cases cited
    if cited:
        api_info = canlii_api_call(uid, database_id, cases_cited=True)
        citation_info.update(api_info)

    ### Cases citing
    if citing:
        api_info = canlii_api_call(uid, database_id, cases_citing=True)
        citation_info.update(api_info)

    return citation_info
