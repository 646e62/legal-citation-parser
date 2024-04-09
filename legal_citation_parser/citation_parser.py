"""
Extracts metadata information from legal citation strings.

"""

from .canlii_rules import canlii_citation_parser

def parse_citation(
    citation: str, citation_type: str = "canlii", **kwargs
) -> dict:
    """
    Parses a citation string to extract key information about the court case.

    Args:
        citation (str): The citation string to parse.
        type (str): The type of citation to parse. Default is "canlii".

    Keyword Args:
        include_url (bool): A flag to determine whether to include the CanLII URL in the output.
        

    Returns:
        dict: A dictionary containing the parsed information, including the style of cause,
        citation, citation type (neutral or CanLII), year, court code, decision number,
        jurisdiction, court name, and court level.
    """

    if citation_type == "canlii":
        return canlii_citation_parser(citation, **kwargs)

    elif "CanLII" in citation:
        return canlii_citation_parser(citation **kwargs)

    else:
        return None
