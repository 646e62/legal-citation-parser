"""
Rule set for parsing CanLII citations and constructing CanLII URLs, as well as neutral citations.
"""

import re

from .canlii_constants import (
    COURT_HIERARCHY_CRIMINAL,
    COURT_LEVEL_MAPPING,
    COURT_LEVEL_MAPPING_LEGACY,
    PROVINCE_TERRITORY_ABBREVIATIONS,
)

from .utils import check_url, canlii_api_call


def court_code_corrector(court_code):
    """
    Court code fine-tuning function to ensure consistency in the court code format.

    Args:
        court_code (str): The court code to correct.

    Returns:
        str: The corrected court code.
    """

    court_code = court_code.lower()

    # Correct for older decisions that use "NWT" instead of "NT"
    if "nwt" in court_code:
        court_code = court_code.replace("nwt", "nt")

    # Format the court code by removing spaces and parentheses
    court_code = court_code.replace("(", "").replace(")", "").replace(" ", "")
    return court_code


def canlii_citation_parser(
    citation_string: str,
    include_url: bool = False,
    call_api_metadata: bool = False,
    call_api_cases_cited: bool = False,
    call_api_cases_citing: bool = False,
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
    citation_string = citation_string.replace(" (CanLII)", "")

    # Absent a very unusually-named court case, the style of cause will always be separated from the
    # rest of the citation by a comma, space, a four-digit year, and another space. This regex
    # pattern captures the style of cause.
    try:
        year = re.search(r", \d{4}", citation_string)
        year = year.group().replace(", ", "")
    except AttributeError:
        year = None

    # Split the string where a comma is followed by a space and then four digits using regex
    # Append the year plus a space to the second element of the resulting list
    citation_string = re.split(r", \d{4} ", citation_string)

    # Extract and format the style of cause
    style_of_cause = citation_string[0]
    style_of_cause = style_of_cause.replace(".", "")

    # Construct the citation string
    try:
        citation = year + " " + citation_string[1]
    except TypeError:
        citation = None

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
        court_code = citation.split(" ")[1]
        court_code = court_code_corrector(court_code)
        decision_number = citation.split(" ")[2]
        uid = generate_uid(year, court_code, decision_number, citation_type)
    
    # Catches CanLII citations in obvious cases where the citation type wasn't explicitly stated
    elif citation and " CanLII " in citation:
        citation_type = "canlii"
        court_code = re.search(r"\(([^)]+)\)", citation)
        court_code = court_code.group()
        court_code = court_code_corrector(court_code)
        decision_number = citation.split(" ")[2]
        uid = generate_uid(year, court_code, decision_number, citation_type)
    else:
        citation_type = None
        court_code = None
        decision_number = None
        uid = None

    # Without this code, the function returns the non-compliant string as the style of cause
    if uid is None:
        style_of_cause = None

    # Extrapolate the court name and jurisdiction from the court code
    if court_code:
        print(court_code)
        court_code_lower = court_code.lower()
        court_decoded = COURT_LEVEL_MAPPING.get(court_code_lower)
        print(court_decoded)
        if court_decoded is None:
            court_decoded = COURT_LEVEL_MAPPING_LEGACY.get(court_code_lower, 'scc')
            print(court_decoded)
        court_level = COURT_HIERARCHY_CRIMINAL.get(court_code_lower)
        court_name = court_decoded[0]
        jurisdiction = court_decoded[1]
    
    # Each subsequent variable requires court_code, so they are set to None if court_code == None
    else:
        court_decoded = court_name = court_level = jurisdiction = None

    # Construct the citation information dictionary
    citation_info = {
        "uid": uid,
        "style_of_cause": style_of_cause,
        "atomic_citation": citation,
        "citation_type": citation_type,
        "scr_citation": scr_citation,
        "year": year,
        "court": court_code,
        "decision_number": decision_number,
        "jurisdiction": jurisdiction,
        "court_name": court_name,
        "court_level": court_level,
    }

    # Include the CanLII URL if requested (off by default)
    if include_url:
        citation_info["url"] = canlii_url_constructor(
            jurisdiction, court_code, year, decision_number, citation_type
        )

    # API non-exclusive fine-tuning
    # Metadata
    if call_api_metadata:
        api_info = canlii_api_call(uid, court_code, decision_metadata=True)
        citation_info.update(api_info)
    
    # Cases the decision cites
    if call_api_cases_cited:
        api_info = canlii_api_call(uid, court_code, cases_cited=True)
        citation_info.update(api_info)

    # Cases that cite the decision
    if call_api_cases_citing:
        api_info = canlii_api_call(uid, court_code, cases_citing=True)
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


def canlii_url_constructor(
    jurisdiction: str,
    court_level: str,
    year: str,
    decision_number: str,
    citation_type: str,
) -> str:
    """
    Constructs the likely URL for a CanLII case based on the jurisdiction, court level, year, and
    decision number. In cases where the decision's URL doesn't follow normal conventions, the
    function will return None.

    Args:
        jurisdiction (str): The jurisdiction abbreviation.
        court_level (str): The court level abbreviation.
        year (str): The year of the decision.
        decision_number (str): The decision number.

    Returns:
        str: The constructed URL for the CanLII case, or None if the URL is invalid.
    """

    if jurisdiction in PROVINCE_TERRITORY_ABBREVIATIONS:
        jurisdiction_code = PROVINCE_TERRITORY_ABBREVIATIONS[jurisdiction]
    else:
        return None
    
    if court_level == "pesc":
        court_level == "pesctd"

    print(court_level)

    # Creates either a CanLII or neutral citation based on the citation type
    citation = generate_uid(year, court_level, decision_number, citation_type)

    # Special case rules for certain jurisdictions and court levels
    # Replace with a more general solution as more exceptions manifest
    
    # court_level
    if "pesc" in court_level:
        court_level = court_level.replace("pesc", "pesctd")
    if "peca" in court_level:
        court_level = court_level.replace("peca", "pescad")
    
    # citation
    if "nt" in citation:
        citation = citation.replace("nt", "nwt")

    # Construct the URL for the English and French versions of the CanLII URL
    urls = [
        (
            f"https://www.canlii.org/en/{jurisdiction_code}/"
            f"{court_level}/doc/{year}/{citation}/{citation}.html"
        ),
        (
            f"https://www.canlii.org/fr/{jurisdiction_code}/"
            f"{court_level}/doc/{year}/{citation}/{citation}.html"
        ),
    ]

    if jurisdiction == "qc":  # Prioritize French URLs for Quebec decisions
        urls.reverse()
    for url in urls:
        if check_url(url):
            return url
    return None

def correct_database_id(court_level: str) -> str:
    """
    Constructs the CanLII database ID for a specific court level.

    Args:
        court_level (str): The court level abbreviation.

    Returns:
        str: The database ID for the court level.
    """

    COURT_CODE_DATABASE_ID_MAPPING = {
        "scc": "csc-scc",
        "scc-l": "csc-scc-al",
        "pesc": "pesctd",
        "peca": "pescad",
        "nuwcat": "ntwcat",
        #9 NBSEC
    }

    if court_level in PROVINCE_TERRITORY_ABBREVIATIONS:
        jurisdiction_code = PROVINCE_TERRITORY_ABBREVIATIONS[court_level]
    else:
        return None

    return f"{jurisdiction_code}/{court_level}" 


def correct_citation(citation: str) -> str:
    """
    Corrects the citation string to ensure consistency in the format.

    Args:
        citation (str): The citation string to correct.

    Returns:
        str: The corrected citation string.
    """

    CITATION_CORRECTION_MAPPING = {
        "nt": "nwt",
        "qcopodq": "qccdpod",
        "qccmmtq": "qccmpmq",
        "nuwcat": "ntnuwcat",
        "ntwcat": "ntnuwcat",
        #9 NBSEC
    }