# legal_citation_parser v 0.2.1
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

In Python 3.x:

```python
>>> from legal_citation_parser import parse_citation
```

Example call:

```python
parse_citation("R v Sutherland, 2022 MBCA 23", include_url=True, call_api_metadata=True)
```

Should produce:

```python
{'uid': '2022mbca23',
 'style_of_cause': 'R v Sutherland',
 'atomic_citation': '2022 MBCA 23',
 'citation_type': 'neutral',
 'scr_citation': None,
 'year': '2022',
 'court': 'mbca',
 'decision_number': '23',
 'jurisdiction': 'manitoba',
 'court_name': 'Court of Appeal of Manitoba',
 'court_level': 'provincial appellate',
 'url': 'https://www.canlii.org/en/mb/mbca/doc/2022/2022mbca23/2022mbca23.html',
 'short_url': 'https://canlii.ca/t/jmnrg',
 'language': 'en',
 'docket_number': 'AR21-30-09591',
 'decision_date': '2022-02-24',
 'keywords': 'Criminal law — Murder — Second degree murder — Evidence — Admissibility',
 'categories': 'Criminal or statutory infractions — Evidence — Practice and procedure'}
```

Example call:

```python
parse_citation("R v Sutherland, 2022 MBCA 23", call_api_cases_cited=True)
```

Should produce:

```python
{'uid': '2022mbca23',
 'style_of_cause': 'R v Sutherland',
 'atomic_citation': '2022 MBCA 23',
 'citation_type': 'neutral',
 'scr_citation': None,
 'year': '2022',
 'court': 'mbca',
 'decision_number': '23',
 'jurisdiction': 'manitoba',
 'court_name': 'Court of Appeal of Manitoba',
 'court_level': 'provincial appellate',
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

## Contributing

Contributions to improve this module are welcome. You can contribute by:
* Reporting bugs
* Suggesting enhancements
* Sending pull requests with bug fixes or new features

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](https://github.com/646e62/legal_citation_parser/blob/main/LICENSE) file for details.

