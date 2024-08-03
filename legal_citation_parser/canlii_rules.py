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


def check_court_code(year, court_code, uid, language="en"):
    """
    Check the court code to determine whether it is a valid CanLII court code. If the court code
    is valid, determine whether it runs into any exceptions. Return the correct database ID.
    
    If the court code is not valid, return None.

    Args:
        year (str): The year of the decision. Used to check for an obscure exception.
        court_code (str): The court code of the decision.
        uid (str): The unique identifier of the decision. Used to check for an obscure exception.
        language (str): The language of the decision. Used to check for an obscure exception.

    Returns:
        str: The database ID of the court code.
    """

    # Check the court code against the COURT_CODE_MAP and return the database ID
    # If the court code is not found, return None
    for court in COURT_CODE_MAP:
        if court_code == court[0]:
            database_id = court[1]
            break
    else:
        database_id = None

    # The QCCMQ database took over "qc cm" after and including 1983, with one exception
    # (1983canlii2659)
    if court_code == "qc cm" and int(year) >= 1983 and uid != "1983canlii2659":
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

    return database_id


def identify_court(database_id: str, language: str) -> tuple:
    """
    Identify the court level, jurisdiction, and court name based on the database ID.

    Args:
        database_id (str): The database ID of the court code.
        language (str): The language of the decision.

    Returns:
        str: The court level of the decision.
        str: The jurisdiction of the decision.
        str: The court name of the decision.
    """

    if database_id:
        court_level = COURT_CODES[database_id]["court_type"]
        jurisdiction = COURT_CODES[database_id]["jurisdiction"]

        # Default to French for Quebec decisions for now
        if jurisdiction == "qc":
            language = "fr"

        court_name = COURT_CODES[database_id]["name"][language]
    else:
        court_level = None
        jurisdiction = None
        court_name = None

    return court_level, jurisdiction, court_name


def generate_uid(
    year: str, court_level: str, decision_number: str, citation_type: str
) -> str:
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

    uid = ""

    if citation_type == "canlii":
        uid = f"{year}canlii{decision_number}"
    else:
        uid = f"{year}{court_level}{decision_number}"

    return uid


def search_right_to_left(pattern: str, text: str) -> tuple:
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


def detect_official_reporter(citation: list) -> tuple:
    """
    Detect the official reporter citation in the citation string. The official reporter citation
    is typically the last element in the citation string, but there are exceptions. This function
    captures the official reporter citation and separates it from the rest of the citation.

    Args:
        citation (list): The citation string split into components.

    Returns:
        official_reporter_citation (str): The official reporter citation.
        citation (str): The rest of the citation.
    """
    OFFICIAL_REPORTER_LIST = [
        "SCR",
        "RCS",
        "CF",
        "FC",
        "CMAR",
        "CACM",
        "Ex CR",
    ]

    for reporter in OFFICIAL_REPORTER_LIST:
        if reporter in citation[1]:
            official_reporter_citation = citation[-1]
            citation = citation[0]
            return official_reporter_citation, citation

    official_reporter_citation = None

    return official_reporter_citation, citation


def verify_citation_year(citation: str) -> str:
    """
    Verify the year of the citation by searching for a four-digit number followed by a comma and
    space. This function is used to extract the year from the citation string.

    Args:
        citation (str): The citation string to parse.

    Returns:
        str: The year of the citation.
    """

    # Modified regex pattern to include checking for an alpha character after the year
    pattern = r", \d{4} "

    # Use the modified search function
    year_match = search_right_to_left(pattern, citation)

    if year_match is None:
        year = None
        return year
    else:
        # Extract the year and the character
        year = year_match[1].replace(", ", "").strip()
        return year


def citation_metadata(year: str, citation: str, language: str ="en") -> tuple:
    """
    Extract metadata information from the citation string. This function is used to infer the
    citation type, court code, official reporter citation, court level, jurisdiction, court name,
    and unique identifier (UID) from the citation string.

    Args:
        year (str): The year of the decision.
        citation (str): The citation string to parse.
        language (str): The language of the decision.

    Returns:
        citation_type (str): The type of citation (neutral or CanLII).
        court_code (str): The court code of the decision.
        official_reporter_citation (str): The official reporter citation.
        court_level (str): The court level of the decision.
        jurisdiction (str): The jurisdiction of the decision.
        court_name (str): The name of the court.
        uid (str): The unique identifier of the decision.
        decision_number (str): The decision number.
        citation (str): The atomic citation
    """

    # Determine the citation type and court code
    if citation and " CanLII " not in citation:
        citation_type = "neutral"
        court_code = citation.split(" ")[1].lower()
    elif citation and " CanLII " in citation:
        citation_type = "canlii"
        court_code = re.search(r"\(([^)]+)\)", citation).group(1).lower()
    else:
        citation_type = None
        court_code = None
        #alert_log.append("Error: citation type not recognized")

    # Identify and separate the official reporter citation from the atomic citation
    if citation and ", " in citation:
        citation_components = citation.split(", ")
        official_reporter_citation, citation = detect_official_reporter(
            citation_components
        )

    else:
        official_reporter_citation = None

    # Extract the decision number and generate the unique identifier
    if citation:
        try:
            decision_number = citation.split(" ")[2]
        except IndexError:
            decision_number = None
            #alert_log.append("Error: decision number not found")

    # Generate the unique identifier and identify the court level, jurisdiction, and court name
    if court_code and decision_number and citation_type:
        uid = generate_uid(year, court_code, decision_number, citation_type)
        uid = uid.replace(",", "")
        database_id = check_court_code(year, court_code, uid)
        court_level, jurisdiction, court_name = identify_court(
            database_id, language
        )
    else:
        uid = None
        court_level = None
        jurisdiction = None 
        court_name = None
        decision_number = None
        #alert_log(f"Error: court code {court_code} not recognized")

    return (
        citation_type,
        court_code,
        official_reporter_citation,
        court_level,
        jurisdiction,
        court_name,
        uid,
        decision_number,
        citation
    )


def separate_citation_elements(citation: str) -> tuple:
    """
    Separate the style of cause from the rest of the citation.

    Args:
        citation (str): The citation string to parse.

    Returns:
        style_of_cause (str): The style of cause.
        citation (str): The rest of the citation.
    """

    try:
        citation = citation.replace(" (CanLII)", "")
        split_citation = re.split(r"(, \d{4} )", citation)
        style_of_cause = split_citation[0].replace(".", "")
        citation = split_citation[1].replace(", ", "") + split_citation[2]
    except IndexError:
        style_of_cause = None
        citation = None
        #alert_log("Error: citation string must contain a style of cause")

    return style_of_cause, citation


def canlii_citation_parser(
    citation: str,
    language: str = "en",
    metadata: bool = False,
    cited: bool = False,
    citing: bool = False,
    verify_url: bool = True,
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

    alert_log = []
    diagnostic_log = []

    year = verify_citation_year(citation)
    style_of_cause, citation = separate_citation_elements(citation)

    # Generate the bulk of the metadata using the inference function
    (
        citation_type,
        court_code,
        official_reporter_citation,
        court_level,
        jurisdiction,
        court_name,
        uid,
        decision_number,
        atomic_citation
    ) = citation_metadata(year, citation)

    # Verify the court code and generate the database ID if possible
    if year and court_code and uid:
        database_id = check_court_code(year, court_code, uid)
    else:
        database_id = None
        #alert_log.append("Error: year not found")

    # Construct the long URL
    if year and language and jurisdiction and database_id and year and uid:
        long_url = f"https://www.canlii.org/{language}/{jurisdiction}/{database_id}/doc/{year}/{uid}/{uid}.html"
    else:
        long_url = None

    # Construct the citation information dictionary
    citation_info = {
        "uid": uid,
        "style_of_cause": style_of_cause,
        "atomic_citation": atomic_citation,
        "citation_type": citation_type,
        "official_reporter_citation": official_reporter_citation,
        "year": year,
        "court": database_id,
        "decision_number": decision_number,
        "jurisdiction": jurisdiction,
        "court_name": court_name,
        "court_level": court_level,
        "long_url": long_url,
        "url_verified": False,
    }

    # Kwargs

    ## Utility
    ### Long URL verification
    if verify_url:
        if check_url(long_url):
            citation_info["url_verified"] = True
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
                citation_info["url_verified"] = True
                print("Alt URL is valid")
            else:
                citation_info["url_verified"] = False
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
