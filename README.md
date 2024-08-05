# legal-citation-parser v 0.5.1
Extracts metadata from CanLII case citations and provides a basic CLI UI for the CanLII API.

Although legal citations are typically short strings, they contain a great deal of information compressed into a relatively small package. This Python module is designed to extract and standardize that data from from legal citation strings. This module can currently handles the following citation types:

* Neutral citations (Canadian);
* Supreme Court Reader (SCR) citations;
* CanLII citations.

Version 0.5.x introduces several new features with significant behind-the-scenes improvements. Most importantly, all of the code has been refactored to work with a class structure for a Citation object, rather than as a simple set of functions that return a dictionary/JSON file. This allows for more flexibility and scalability in the future while solving numerous bugs and issues present in previous versions.

Version 0.5.1 fixes an error that caused some functions to fail, rather than return None values, for erroneous parser results.


## Metadata

### Basic citation string

The module currently extracts the following from raw CanLII citation strings:

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
- **URL verified.** Verifies whether the CanLII URL returns a 200 status code.
- **Error.** Records errors and other alerts encountered during the parsing process.

### CanLII API

The module is also able to use the CanLII API to retrieve additional metadata and other potentially useful case information, including:

* **Short URL.** The decision's short URL.
* **Language.** The decision's language or languages.
* **Docket number.** The decision's docket number or numbers.
* **Decision date.** The YYYY-MM-DD the court issued the decision.
* **Keywords.** A 'list' of keywords supplied by CanLII, separated by a '—'.
* **Categories.** A 'list' of categories supplied by CanLII, also separated by a '—'.
* **Cases cited.** A list of decisions (including databaseId, caseId, title, and citation) the case cites.
* **Cases citing.** A list of decisions (including databaseId, caseId, title, and citation) that cite the case.

## Installation

### pip

From the command line:

```bash
pip install legal_citation_parser
```

## Usage

In Python 3.x:

```python
>>> from legal_citation_parser import parse_citation
```

### Kwargs
* `verify_url`: Pings a program-generated `long_url` . If unsuccessful, the function checks the same URL with the alternative language selected (i.e., "fr" instead of "en", and vice versa). Returns `None` if neither URL ping successfully.
* `metadata`: Retrieves CanLII metadata. Requires a CanLII API key.
* `cited`:  Returns a list of cases a decision cites. Requiees a CanLII API key.
* `citing`: Returns a list of cases that cite the decision. Requires a CanLII API key.

### Example calls

Example call:

```python
parse_citation("R v Sutherland, 2022 MBCA 23", verify_url=True, metadata=True)
```

Should produce:

```python
{'uid': '2022mbca23',
 'style_of_cause': 'R v Sutherland',
 'atomic_citation': '2022 MBCA 23',
 'citation_type': 'neutral',
 'official_reporter_citation': None,
 'year': '2022',
 'court': 'mbca',
 'decision_number': '23',
 'jurisdiction': 'mb',
 'court_name': 'Court of Appeal of Manitoba',
 'court_level': 'provincial appellate',
 'long_url': 'https://www.canlii.org/en/mb/mbca/doc/2022/2022mbca23/2022mbca23.html',
 'url_verified': True,
 'short_url': 'https://canlii.ca/t/jmnrg',
 'language': 'en',
 'docket_number': 'AR21-30-09591',
 'decision_date': '2022-02-24',
 'keywords': ['Criminal law',
  'Murder',
  'Second degree murder',
  'Evidence',
  'Admissibility'],
 'categories': ['Criminal or statutory infractions',
  'Evidence',
  'Practice and procedure'],
 'cited_cases': [],
 'citing_cases': [],
 'error': None}
```

Example call:

```python
parse_citation("R v Sutherland, 2022 MBCA 23", cited=True)
```

Should produce:

```python
{'uid': '2022mbca23',
 'style_of_cause': 'R v Sutherland',
 'atomic_citation': '2022 MBCA 23',
 'citation_type': 'neutral',
 'official_reporter_citation': None,
 'year': '2022',
 'court': 'mbca',
 'decision_number': '23',
 'jurisdiction': 'mb',
 'court_name': 'Court of Appeal of Manitoba',
 'court_level': 'provincial appellate',
 'long_url': 'https://www.canlii.org/en/mb/mbca/doc/2022/2022mbca23/2022mbca23.html',
 'url_verified': False,
 'short_url': None,
 'language': 'en',
 'docket_number': None,
 'decision_date': None,
 'keywords': [],
 'categories': [],
 'cited_cases': {'citedCases': [{'databaseId': 'csc-scc',
    'caseId': {'en': '1956canlii541'},
    'title': 'Chibok v. The Queen',
    'citation': '1956 CanLII 541 (SCC)'},
   {'databaseId': 'nbca',
    'caseId': {'en': '2021nbca3'},
    'title': 'Currie v. R.',
    'citation': '2021 NBCA 3 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '1982canlii33'},
    'title': 'Graat v. The Queen',
    'citation': '1982 CanLII 33 (SCC), [1982] 2 SCR 819'},
   {'databaseId': 'onca',
    'caseId': {'en': '2018onca494'},
    'title': 'R. v. Ajise',
    'citation': '2018 ONCA 494 (CanLII)'},
    ...
   } 
```

```python
create_citation("R v Sutherland, 2022 MBCA 23")
```

Should produce a Citation object containing all of the above citation metadata. Once created, the object can be used to access the metadata in the same way as the API call by using the ```parse``` method.

Example call:

```python
citation = create_citation("R v Sutherland, 2022 MBCA 23", verify_url=True, metadata=True)
citation.parse()
```

Should produce: 

```python
{'uid': '2022mbca23',
 'style_of_cause': 'R v Sutherland',
 'atomic_citation': '2022 MBCA 23',
 'citation_type': 'neutral',
 'official_reporter_citation': None,
 'year': '2022',
 'court': 'mbca',
 'decision_number': '23',
 'jurisdiction': 'mb',
 'court_name': 'Court of Appeal of Manitoba',
 'court_level': 'provincial appellate',
 'long_url': 'https://www.canlii.org/en/mb/mbca/doc/2022/2022mbca23/2022mbca23.html',
 'url_verified': True,
 'short_url': 'https://canlii.ca/t/jmnrg',
 'language': 'en',
 'docket_number': 'AR21-30-09591',
 'decision_date': '2022-02-24',
 'keywords': ['Criminal law',
  'Murder',
  'Second degree murder',
  'Evidence',
  'Admissibility'],
 'categories': ['Criminal or statutory infractions',
  'Evidence',
  'Practice and procedure'],
 'cited_cases': [],
 'citing_cases': [],
 'error': None}
 ```

 Individual attributes are callable from the Citation object:

 ```python
 >>> citation.uid
 '2022mbca23'
 >>> citation.court_level
 'provincial appellate'
 >>> citation.keywords
 ['Criminal law', 'Murder', 'Second degree murder', 'Evidence', 'Admissibility']
 ```

## v 0.5.0 updates

* Refactored all of the code to work with a class structure, with a focus on the Citation object

## Contributing

Contributions to improve this module are welcome. You can contribute by:
* Reporting bugs
* Suggesting enhancements
* Sending pull requests with bug fixes or new features

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](https://github.com/646e62/legal_citation_parser/blob/main/LICENSE) file for details.
