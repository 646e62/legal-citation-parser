"""
Rule set for parsing CanLII citations and constructing CanLII URLs, as well as neutral citations.
"""

import re
import os
import sys
import requests

from dotenv import load_dotenv

from .canlii_constants import (
    COURT_HIERARCHY_CRIMINAL,
    COURT_LEVEL_MAPPING,
    PROVINCE_TERRITORY_ABBREVIATIONS,
)

from .utils import check_url


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
    if citation and " CanLII " not in citation:
        citation_type = "neutral"
        court_code = citation.split(" ")[1]
        court_code = court_code_corrector(court_code)
        decision_number = citation.split(" ")[2]
        uid = str(year) + court_code + decision_number
    elif citation and " CanLII " in citation:
        citation_type = "canlii"
        court_code = re.search(r"\(([^)]+)\)", citation)
        court_code = court_code.group()
        court_code = court_code_corrector(court_code)
        decision_number = citation.split(" ")[2]
        uid = str(year) + court_code + decision_number
    else:
        citation_type = None
        court_code = None
        decision_number = None
        uid = None

    if uid is None:
        style_of_cause = None

    # Extrapolate the court name and jurisdiction from the court code
    if court_code:
        court_code_lower = court_code.lower()
        court_decoded = COURT_LEVEL_MAPPING.get(court_code_lower)
        court_level = COURT_HIERARCHY_CRIMINAL.get(court_code_lower)
        court_name = court_decoded[0]
        jurisdiction = court_decoded[1]
    else:
        court_decoded = None
        court_name = None
        court_level = None
        jurisdiction = None
        court_name = None
        jurisdiction = None

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

    # API fine-tuning
    if call_api_metadata:
        api_info = canlii_api_call(uid, court_code, get_metadata=True)
        citation_info.update(api_info)
    
    if call_api_cases_cited:
        api_info = canlii_api_call(uid, court_code, get_cited_cases=True)
        citation_info.update(api_info)

    if call_api_cases_citing:
        api_info = canlii_api_call(uid, court_code, get_citing_cases=True)
        citation_info.update(api_info)

    return citation_info


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

    # Creates either a CanLII or neutral citation based on the citation type
    if citation_type == "canlii":
        citation = f"{year}canlii{decision_number}"
    else:
        citation = f"{year}{court_level}{decision_number}"

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


def canlii_api_call(
    case_id: str,
    database_id: str,
    language: str = "en",
    get_metadata=False,
    get_cited_cases=False,
    get_citing_cases=False,
) -> dict:
    """
    Makes an API call to the CanLII API to retrieve metadata information about a case.

    Args:
        case_id (str): The unique CanLII case ID.

    Returns:
        dict: A dictionary containing the metadata information about the case, including the style
        of cause, citation, citation type (neutral or CanLII), year, court code, decision number,
        jurisdiction, court name, and court level. The dictionary will also include the CanLII URL.
    """

    # Load the CanLII API key from the .env file. If it is not present, prompt the user to enter it.
    # If the user enters nothing, the function will exit.

    
    load_dotenv()
    if os.getenv("CANLII_API_KEY") is None:
        print("Please enter your CanLII API key (or blank input to exit):")
        API_KEY = input()
        if API_KEY == "":
            sys.exit()
    else:
        API_KEY = os.getenv("CANLII_API_KEY")

    metadata_api_info = {}

    if database_id == "scc":
        database_id = "csc-scc"

    if get_metadata:
        metadata_url = f"https://api.canlii.org/v1/caseBrowse/{language}/{database_id}/{case_id}/?api_key={API_KEY}"
        response = requests.get(metadata_url, timeout=5)
        case_metadata = response.json()
        metadata_api_info["short_url"] = case_metadata["url"]
        metadata_api_info["language"] = case_metadata["language"]
        metadata_api_info["docket_number"] = case_metadata["docketNumber"]
        metadata_api_info["decision_date"] = case_metadata["decisionDate"]
        metadata_api_info["keywords"] = case_metadata["keywords"]
        metadata_api_info["categories"] = case_metadata["topics"]

    if get_cited_cases:
        cited_cases_url = f"  https://api.canlii.org/v1/caseCitator/{language}/{database_id}/{case_id}/citedCases?api_key={API_KEY}"
        response = requests.get(cited_cases_url, timeout=5)
        cited_cases = response.json()
        metadata_api_info["cited_cases"] = cited_cases

    if get_citing_cases:
        citing_cases_url = (
            cited_cases_url
        ) = f"  https://api.canlii.org/v1/caseCitator/{language}/{database_id}/{case_id}/citingCases?api_key={API_KEY}"
        response = requests.get(citing_cases_url, timeout=5)
        citing_cases = response.json()
        metadata_api_info["citing_cases"] = citing_cases

    return metadata_api_info
