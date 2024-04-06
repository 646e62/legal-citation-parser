# legal_citation_parser
Extracts metadata from legal citations.

Although legal citations are typically short strings, they contain a great deal of information compressed into a relatively small package. This Python module is designed to extract and standardize that data from from legal citation strings. This module can currently handles the following citation types:

* Neutral citations (Canadian);
* Supreme Court Reader (SCR) citations;
* CanLII citations.

## Features

- **Citation parsing.** The module extracts the following metadata from raw CanLII citation strings:
  - Atomic citation
  - Style of cause
  - Citation type
  - Year
  - Decision number
  - Jurisdiction
  - Court name
  - Court level
  - CanLII URL

## Known issues
- Assumes and requires correct input
- Currently limited to neutral and CanLII citations


## Installation

From the command line:

```bash
pip install legal_citation_parser
```

In Python 3.x:

```python
>>> from legal_citation_parser import parse_citation
```

## Contributing

Contributions to improve this module are welcome. You can contribute by:
* Reporting bugs
* Suggesting enhancements
* Sending pull requests with bug fixes or new features

## License

This project is licensed under the GPL 3.0 License - see the LICENSE file for details.

