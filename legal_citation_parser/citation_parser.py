# citation_parser.py

from .canlii_rules import CanLIICitationParser

def create_citation(citation: str, citation_type: str = "canlii", **kwargs) -> dict:
    """
    Creates a citation object from a citation string.

    Args:
        citation (str): The citation string to parse.
        type (str): The type of citation to parse. Default is "canlii".

    Keyword Args:
        include_url (bool): A flag to determine whether to include the CanLII URL in the output.
        

    Returns:
        ParsedCitation: An object containing the parsed information, including the style of cause,
        citation, citation type (neutral or CanLII), year, court code, decision number,
        jurisdiction, court name, and court level.
    """

    parser = CanLIICitationParser(citation, **kwargs)
    citation_info = parser.parse()
    
    return citation_info


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
        ParsedCitation: An object containing the parsed information, including the style of cause,
        citation, citation type (neutral or CanLII), year, court code, decision number,
        jurisdiction, court name, and court level.
    """

    citation_info = create_citation(citation, citation_type, **kwargs)
    
    return citation_info.full()
