# legal_citation_parser
Extracts metadata from legal citations.

This Python module is designed to extract and standardize metadata from legal citation strings specifically from the Canadian Legal Information Institute (CanLII) database. It includes functionalities such as validating URLs, correcting court codes, parsing citation strings, and constructing URLs based on the extracted metadata.

## Features

- **Citation parsing**: Extracts metadata from CanLII citation strings, including court name, court level, jurisdiction, and more.
- **URL construction**: Constructs CanLII URLs for cases based on their metadata.

## Known issues
- Assumes and requires correct input
- Currently limited to neutral and CanLII citations


## Installation

```bash
pip install legal_citation_parser
```

```python
from legal_citation_parser import parse_citation
```

## Contributing

Contributions to improve this module are welcome. You can contribute by:
* Reporting bugs
* Suggesting enhancements
* Sending pull requests with bug fixes or new features

## License

This project is licensed under the GPL 3.0 License - see the LICENSE file for details.

