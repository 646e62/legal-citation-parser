"""
Shared utility functions for the legal citation parser.
"""

import requests
import os
import sys
import requests

from dotenv import load_dotenv

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
    case_id: str,
    legislation_id: str,
    database_id: str,
    language: str = "en",
    decision_metadata=False,
    legislation_metadata=False,
    cases_cited=False,
    cases_citing=False,
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

    if database_id == "scc":
        database_id = "csc-scc"

    if decision_metadata:
        metadata_url = f"https://api.canlii.org/v1/caseBrowse/{language}/{database_id}/{case_id}/?api_key={API_KEY}"
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

    return metadata_api_info
