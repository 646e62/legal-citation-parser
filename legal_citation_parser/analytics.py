# analytics.py

"""
Analytic functions for the legal citation parser.
"""

from collections import Counter
from .citation_parser import parse_citation

def parse_case_list(case_list: list) -> list:
    """
    Parses a list of case citations to extract key information about the court cases.

    Args:
        case_list (list): A list of citation strings to parse.

    Returns:
        list: A list of dictionaries containing the parsed information for each case,
        including the style of cause, citation, citation type (neutral or CanLII), year,
        court code, decision number, jurisdiction, court name, and court level.
    """

    case_list_parsed = []

    for case in case_list:
        case_info = parse_citation(case["title"] + ", " + case["citation"])
        case_list_parsed.append(case_info)

    return case_list_parsed

def count_jurisdictions(case_list: list) -> dict:
    """
    Counts the number of cases from each jurisdiction in a list of parsed cases.

    Args:
        case_list (list): A list of parsed case dictionaries.

    Returns:
        dict: A dictionary where the keys are the jurisdiction names and the values are the
        number of cases from each jurisdiction.
    """

    jurisdictions = [case["jurisdiction"] + " " + case["court_level"] for case in case_list]
    jurisdiction_counts = Counter(jurisdictions)

    return jurisdiction_counts

