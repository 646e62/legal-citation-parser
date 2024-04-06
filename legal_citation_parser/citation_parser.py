"""
This Python module provides tools for extracting metadata information from legal citation strings.

"""

# from canlii_rules import canlii_citation_parser

from .canlii_rules import canlii_citation_parser

# Main code


def parse_citation(
    citation: str, citation_type: str = "canlii", include_url: bool = False
) -> dict:
    """
    Parses a citation string to extract key information about the court case.

    Args:
        citation (str): The citation string to parse.
        type (str): The type of citation to parse. Default is "canlii".

    Returns:
        dict: A dictionary containing the parsed information, including the style of cause,
        citation, citation type (neutral or CanLII), year, court code, decision number,
        jurisdiction, court name, and court level.
    """

    if citation_type == "canlii":
        return canlii_citation_parser(citation, include_url=include_url)

    elif "CanLII" in citation:
        return canlii_citation_parser(citation)

    else:
        return None
