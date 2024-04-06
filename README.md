# citation_parser
Extracts metadata from legal citations.

This Python module is designed to extract and standardize metadata from legal citation strings specifically from the Canadian Legal Information Institute (CanLII) database. It includes functionalities such as validating URLs, correcting court codes, parsing citation strings, and constructing URLs based on the extracted metadata.

## Features

- **URL Validation**: Checks if a CanLII URL is valid by sending a GET request.
- **Court Code Correction**: Standardizes and corrects court codes found within citation strings.
- **Citation Parsing**: Extracts metadata from CanLII citation strings, including year, court code, decision number, and more.
- **URL Construction**: Constructs CanLII URLs for cases based on their metadata.

## Known issues
- Assumes and requires correct input
- Currently limited to neutral and CanLII citations

## Installation

To use this module, first ensure you have Python installed on your system. Then, clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/canlii-citation-metadata-extractor.git
cd canlii-citation-metadata-extractor
```
Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```python
from citation_extractor import parse_citation, canlii_url_constructor

citation = "R v Smith, 2019 ONCA 123 (CanLII)"
parsed_citation = parse_citation(citation, citation_type="canlii")

print(parsed_citation)

# To construct a URL from the parsed citation
url = canlii_url_constructor(parsed_citation['jurisdiction'], parsed_citation['court'], parsed_citation['year'], parsed_citation['decision_number'], parsed_citation['citation_type'])

print(url)
```

## Contributing

Contributions to improve this module are welcome. You can contribute by:
* Reporting bugs
* Suggesting enhancements
* Sending pull requests with bug fixes or new features

## License

This project is licensed under the GPL 3.0 License - see the LICENSE file for details.

