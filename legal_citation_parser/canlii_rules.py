"""
Rule set for parsing CanLII citations and constructing CanLII URLs, as well as neutral citations.
"""

import re

from .canlii_constants import (
    COURT_HIERARCHY_CRIMINAL,
    COURT_CODES,
    COURT_CODE_MAP,
)

from .utils import canlii_api_call, check_url

def canlii_citation_parser(
    citation_string: str,
    language: str = "en",
    metadata: bool = False,
    cited: bool = False,
    citing: bool = False,
    verify_url: bool = False,
) -> dict:
    """
    Rules for parsing a CanLII citation string to extract metadata information.

    Args:
        citation_string (str): The CanLII citation string to parse.
        include_url (bool): A flag to determine whether to include the CanLII URL in the output.

    Returns:
        dict: A dictionary containing the parsed information, including the style of cause,
        citation, citation type (neutral or CanLII), year, court code, decision number,
        jurisdiction, court name, and court level. If `include_url` is True, the dictionary will
        also include the CanLII URL.
    """

    # Remove the " (CanLII)" suffix from the citation string, if present, as it is not part of the
    # citation itself

    def check_court_code(court_code, citation, language="en"):
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

        # nwttc/nwtsc & ntwytc — defaulting to NTTC for now
        # Can be addressed with a ping test or the CanLII API later
        elif court_code == "nwttc":
            database_id = "nttc"
        elif court_code == "nwtsc":
            database_id = "ntsc"

        # qcta/qctaa - default to qcta for now
        # Can be addressed with a ping test or the CanLII API later
        elif court_code == "qcta":
            database_id = "qcta"

        # onsc/onsctd - default to onsc for now
        # Can be addressed with a ping test or the CanLII API later
        elif court_code == "onsc":
            database_id = "onsc"

        return uid, decision_number, database_id
    

    def check_court_database(database_id, language):
        """
        DRY function to check the court database ID and return the court level, jurisdiction, and
        court name.
        """
        court_level = COURT_HIERARCHY_CRIMINAL.get(database_id)
        jurisdiction = COURT_CODES[database_id]["jurisdiction"]
    
        # Default to French for Quebec decisions for now
        if jurisdiction == "qc":
            language = "fr"
        
        court_name = COURT_CODES[database_id]["name"][language]

        return court_level, jurisdiction, court_name


    citation_string = citation_string.replace(" (CanLII)", "")

    # Absent a very unusually-named court case, the style of cause will always be separated from the
    # rest of the citation by a comma, space, a four-digit year, and another space. This regex
    # pattern captures the style of cause.
    year_match = re.search(r", \d{4}", citation_string)
    if year_match is None:
        return "Error: citation string must contain a four-digit year"  # If no year is found, return None
    year = year_match.group().replace(", ", "")

    # Split the citation string into the style of cause and the rest of the citation
    citation_string = re.split(r", \d{4} ", citation_string)
    style_of_cause = citation_string[0].replace(".", "")

    # Construct the citation string
    try:
        citation = year + " " + citation_string[1]
    except IndexError:
        return "Error: citation must contain a court code and decision number"

    # Identify and handle SCR citations
    if citation and " SCR " in citation:
        citation = citation.split(", ")
        scr_citation = citation[1]
        citation = citation[0]
    else:
        scr_citation = None

    # Determine the citation type, if any
    # Relocate and refactor this code if more citation types are added
    if citation and " CanLII " not in citation:
        citation_type = "neutral"
        court_code = citation.split(" ")[1].lower()
        uid, decision_number, database_id = check_court_code(court_code, citation, language)
        # Return an error if the court code is not recognized
        if uid is None:
            return "Error: court code not recognized"

    # Catches CanLII citations in obvious cases where the citation type wasn't explicitly stated
    elif citation and " CanLII " in citation:
        citation_type = "canlii"
        court_code = re.search(r"\(([^)]+)\)", citation)
        court_code = court_code.group(1).lower()
        uid, decision_number, database_id = check_court_code(court_code, citation, language)
        if uid is None:
            return "Error: court code not recognized"
    else:
        return None

    # Without this code, the function returns the non-compliant string as the style of cause
    if uid is None:
        return None

    # Compile the long URL
    court_level, jurisdiction, court_name = check_court_database(database_id, language)
    long_url = f"https://www.canlii.org/{language}/{jurisdiction}/{database_id}/doc/{year}/{uid}/{uid}.html"


    # Construct the citation information dictionary
    citation_info = {
        "uid": uid,
        "style_of_cause": style_of_cause,
        "atomic_citation": citation,
        "citation_type": citation_type,
        "scr_citation": scr_citation,
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
