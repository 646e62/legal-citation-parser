"""
Shared utility functions for the legal citation parser.
"""

import requests
import os
import sys
import requests

from dotenv import load_dotenv
from .canlii_constants import PROVINCE_TERRITORY_ABBREVIATIONS

def check_url(url: str) -> str:
    """
    Checks if a URL is valid by sending a GET request and verifying the status code.

    Args:
        url (str): The URL to check.

    Returns:
        str: The URL if it is valid, otherwise None.
    """

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return url
        else:
            return None
    except requests.RequestException:
        return None


def canlii_api_call(
    case_id: str = None,
    database_id: str = None,
    legislation_id: str = None,
    language: str = "en",
    decision_metadata=False,
    legislation_metadata=False,
    cases_cited=False,
    cases_citing=False,
    canlii_database=False,
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

    load_dotenv()
    if os.getenv("CANLII_API_KEY") is None:
        print("Please enter your CanLII API key (or blank input to exit):")
        API_KEY = input()
        if API_KEY == "":
            sys.exit()
    else:
        API_KEY = os.getenv("CANLII_API_KEY")

    metadata_api_info = {}

    # Corrections. Replace with a proper dictionary
    if database_id == "scc":
        database_id = "csc-scc"
    if database_id == "scc-l":
        database_id = "csc-scc-al"

    if decision_metadata:
        metadata_url = f"https://api.canlii.org/v1/caseBrowse/{language}/{database_id}/{case_id}/?api_key={API_KEY}"
        print(metadata_url)
        response = requests.get(metadata_url, timeout=5)
        case_metadata = response.json()
        metadata_api_info["short_url"] = case_metadata["url"]
        metadata_api_info["language"] = case_metadata["language"]
        metadata_api_info["docket_number"] = case_metadata["docketNumber"]
        metadata_api_info["decision_date"] = case_metadata["decisionDate"]
        metadata_api_info["keywords"] = case_metadata["keywords"]
        metadata_api_info["categories"] = case_metadata["topics"]

    if cases_cited:
        cited_cases_url = f"https://api.canlii.org/v1/caseCitator/{language}/{database_id}/{case_id}/citedCases?api_key={API_KEY}"
        response = requests.get(cited_cases_url, timeout=5)
        cited_cases = response.json()
        metadata_api_info["cited_cases"] = cited_cases

    if cases_citing:
        citing_cases_url = (
            cited_cases_url
        ) = f"https://api.canlii.org/v1/caseCitator/{language}/{database_id}/{case_id}/citingCases?api_key={API_KEY}"
        response = requests.get(citing_cases_url, timeout=5)
        citing_cases = response.json()
        metadata_api_info["citing_cases"] = citing_cases

    # Placeholder for legislation metadata
    if legislation_metadata:
        metadata_url = f"https://api.canlii.org/v1/legislationBrowse/{language}/{database_id}/{legislation_id}/?api_key={API_KEY}"
        response = requests.get(metadata_url, timeout=5)
        legislation_metadata = response.json()
        metadata_api_info["database_id"] = legislation_metadata["databaseId"]
        metadata_api_info["legislation_id"] = legislation_metadata["legislationId"]
        metadata_api_info["title"] = legislation_metadata["title"]
        metadata_api_info["type"] = legislation_metadata["type"]
        metadata_api_info["citation"] = legislation_metadata["citation"]

    if canlii_database:
        database_url = f"https://api.canlii.org/v1/caseBrowse/{language}/?api_key={API_KEY}"
        response = requests.get(database_url, timeout=5)
        database_info = response.json()
        metadata_api_info["database"] = database_info

    return metadata_api_info


def generate_canlii_court_database(language: str ="en") -> dict:
    """
    Generates a dictionary of CanLII court databases.

    Args:
        language (str): The language of the court databases.

    Returns:
        dict: A dictionary containing the court databases available on CanLII.
    """

    case_database = canlii_api_call(language=language, canlii_database=True)

    ABBREVIATION_TO_PROVINCE_TERRITORY = {v: k for k, v in PROVINCE_TERRITORY_ABBREVIATIONS.items()}
    transformed_dict = {}
    for entry in case_database:
        database_id = entry.get('databaseId')
        name = entry.get('name')
        jurisdiction = entry.get('jurisdiction')

        # Substitute the jurisdiction with its full name
        jurisdiction_full = ABBREVIATION_TO_PROVINCE_TERRITORY.get(jurisdiction, jurisdiction)  # Default to original if not found
        transformed_dict[database_id] = (name, jurisdiction_full)
    
    return transformed_dict
