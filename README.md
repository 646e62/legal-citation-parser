# legal_citation_parser
Extracts metadata from legal citations.

Although legal citations are typically short strings, they contain a great deal of information compressed into a relatively small package. This Python module is designed to extract and standardize that data from from legal citation strings. This module can currently handles the following citation types:

* Neutral citations (Canadian);
* Supreme Court Reader (SCR) citations;
* CanLII citations.

## Metadata

### Basic citation string

The module currently extracts the following from (most) raw CanLII citation strings:

- **UID.** The decision's unique ID. Corresponds to the CanLII API's `caseId` variable.
- **Atomic citation.** The citation's human readable unique ID. 
- **Style of cause.** The human readable case name.
- **Citation type.** The type of citation parsed.
- **Year.** The decision's year.
- **Decision number.** The decision's number.
- **Jurisdiction.** The province, territory, or federal jurisdiction the case was heard in.
- **Court name.** The human readable court level.
- **Court level.** The relative level of the court.
- **CanLII URL.** The decision's URL on canlii.org

### CanLII API



## Installation

### pip

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

