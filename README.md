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

```python
parse_citation("R v Sutherland, 2022 MBCA 23", call_api_cases_cited=True)
```

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
   {'databaseId': 'csc-scc',
    'caseId': {'en': '1993canlii101'},
    'title': 'R. v. Bevan',
    'citation': '1993 CanLII 101 (SCC), [1993] 2 SCR 599'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2017scc12'},
    'title': 'R. v. Bingley',
    'citation': '2017 SCC 12 (CanLII), [2017] 1 SCR 170'},
   {'databaseId': 'onca',
    'caseId': {'en': '2021onca16'},
    'title': 'R. v. Borel',
    'citation': '2021 ONCA 16 (CanLII)'},
   {'databaseId': 'bcca',
    'caseId': {'en': '2020bcca277'},
    'title': 'R. v. Czechowski',
    'citation': '2020 BCCA 277 (CanLII)'},
   {'databaseId': 'onca',
    'caseId': {'en': '2021onca380'},
    'title': 'R. v. Daou',
    'citation': '2021 ONCA 380 (CanLII)'},
   {'databaseId': 'onca',
    'caseId': {'en': '2017onca609'},
    'title': 'R. v. Douglas',
    'citation': '2017 ONCA 609 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2019scc3'},
    'title': 'R. v. Fedyck',
    'citation': '2019 SCC 3 (CanLII), [2019] 1 SCR 97'},
   {'databaseId': 'onca',
    'caseId': {'en': '2016onca953'},
    'title': 'R. v. H.B.',
    'citation': '2016 ONCA 953 (CanLII)'},
   {'databaseId': 'onca',
    'caseId': {'en': '2016onca284'},
    'title': 'R. v. Hassanzada',
    'citation': '2016 ONCA 284 (CanLII)'},
   {'databaseId': 'onca',
    'caseId': {'en': '1986canlii4722'},
    'title': 'R. v. Hill',
    'citation': '1986 CanLII 4722 (ON CA)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2003mbca20'},
    'title': 'R. v. Ilina',
    'citation': '2003 MBCA 20 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2011scc17'},
    'title': 'R. v. J.A.A.',
    'citation': '2011 SCC 17 (CanLII), [2011] 1 SCR 628'},
   {'databaseId': 'bcca',
    'caseId': {'en': '2013bcca11'},
    'title': 'R. v. James',
    'citation': '2013 BCCA 11 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2001scc86'},
    'title': 'R. v. Khan',
    'citation': '2001 SCC 86 (CanLII), [2001] 3 SCR 823'},
   {'databaseId': 'nsca',
    'caseId': {'en': '2021nsca76'},
    'title': 'R. v. Kotio',
    'citation': '2021 NSCA 76 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '1990canlii95'},
    'title': 'R. v. Lavallee',
    'citation': '1990 CanLII 95 (SCC), [1990] 1 SCR 852'},
   {'databaseId': 'bcca',
    'caseId': {'en': '2015bcca358'},
    'title': 'R. v. Lawrence',
    'citation': '2015 BCCA 358 (CanLII)'},
   {'databaseId': 'abca',
    'caseId': {'en': '2010abca1'},
    'title': 'R. v. Lee',
    'citation': '2010 ABCA 1 (CanLII)'},
   {'databaseId': 'onca',
    'caseId': {'en': '2012onca388'},
    'title': 'R. v. Lewis',
    'citation': '2012 ONCA 388 (CanLII)'},
   {'databaseId': 'onca',
    'caseId': {'en': '2009onca485'},
    'title': 'R.\xa0v.\xa0Manjra',
    'citation': '2009 ONCA 485 (CanLII)'},
   {'databaseId': 'onca',
    'caseId': {'en': '2019onca940'},
    'title': 'R. v. Mills',
    'citation': '2019 ONCA 940 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '1994canlii80'},
    'title': 'R. v. Mohan',
    'citation': '1994 CanLII 80 (SCC), [1994] 2 SCR 9'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2011scc29'},
    'title': "R. v. O'Brien",
    'citation': '2011 SCC 29 (CanLII), [2011] 2 SCR 485'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2014mbca70'},
    'title': 'R. v. Pearce (M.L.)',
    'citation': '2014 MBCA 70 (CanLII)'},
   {'databaseId': 'abca',
    'caseId': {'en': '2006abca267'},
    'title': 'R. v. Powell',
    'citation': '2006 ABCA 267 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2019scc41'},
    'title': 'R. v. R.V.',
    'citation': '2019 SCC 41 (CanLII), [2019] 3 SCR 237'},
   {'databaseId': 'bcca',
    'caseId': {'en': '2012bcca352'},
    'title': 'R. v. Ratté',
    'citation': '2012 BCCA 352 (CanLII)'},
   {'databaseId': 'abca',
    'caseId': {'en': '2006abca411'},
    'title': 'R. v. Sargent',
    'citation': '2006 ABCA 411 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2011scc54'},
    'title': 'R. v. Sarrazin',
    'citation': '2011 SCC 54 (CanLII), [2011] 3 SCR 505'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2014scc15'},
    'title': 'R. v. Sekhon',
    'citation': '2014 SCC 15 (CanLII), [2014] 1 SCR 272'},
   {'databaseId': 'onca',
    'caseId': {'en': '2014onca791'},
    'title': 'R. v. Singh',
    'citation': '2014 ONCA 791 (CanLII)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2014mbca40'},
    'title': 'R. v. T.I.E.',
    'citation': '2014 MBCA 40 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2007scc6'},
    'title': 'R. v. Trochym',
    'citation': '2007 SCC 6 (CanLII), [2007] 1 SCR 239'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2009scc22'},
    'title': 'R. v. Van',
    'citation': '2009 SCC 22 (CanLII), [2009] 1 SCR 716'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2016scc33'},
    'title': 'R. v. Villaroman',
    'citation': '2016 SCC 33 (CanLII), [2016] 1 SCR 1000'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2011scc13'},
    'title': 'R. v. White',
    'citation': '2011 SCC 13 (CanLII), [2011] 1 SCR 433'},
   {'databaseId': 'pescad',
    'caseId': {'en': '2018peca6'},
    'title': 'R. v Gavin',
    'citation': '2018 PECA 6 (CanLII)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2018mbca86'},
    'title': 'R v Banayos and Banayos',
    'citation': '2018 MBCA 86 (CanLII)'},
   {'databaseId': 'abca',
    'caseId': {'en': '2016abca114'},
    'title': 'R v Dominic',
    'citation': '2016 ABCA 114 (CanLII)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2020mbca23'},
    'title': 'R v Dowd',
    'citation': '2020 MBCA 23 (CanLII)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2018mbca74'},
    'title': 'R v Fedyck',
    'citation': '2018 MBCA 74 (CanLII)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2020mbca95'},
    'title': 'R v Herntier',
    'citation': '2020 MBCA 95 (CanLII)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2017mbca72'},
    'title': 'R v McDonald',
    'citation': '2017 MBCA 72 (CanLII)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2021mbca55'},
    'title': 'R v McIvor',
    'citation': '2021 MBCA 55 (CanLII)'},
   {'databaseId': 'skca',
    'caseId': {'en': '2018skca78'},
    'title': 'R v Montague-Mitchell',
    'citation': '2018 SKCA 78 (CanLII)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2019mbca99'},
    'title': 'R v Ponace',
    'citation': '2019 MBCA 99 (CanLII)'},
   {'databaseId': 'mbca',
    'caseId': {'en': '2013canlii83110'},
    'title': 'R v Pruden',
    'citation': '2013 MBCA 107 (CanLII)'},
   {'databaseId': 'skca',
    'caseId': {'en': '2015skca85'},
    'title': 'R v Rahimi',
    'citation': '2015 SKCA 85 (CanLII)'},
   {'databaseId': 'abca',
    'caseId': {'en': '2017abca154'},
    'title': 'R v Sandoval-Barillas',
    'citation': '2017 ABCA 154 (CanLII)'},
   {'databaseId': 'csc-scc',
    'caseId': {'en': '2015scc23'},
    'title': 'White Burgess Langille Inman v. Abbott and Haliburton Co.',
    'citation': '2015 SCC 23 (CanLII), [2015] 2 SCR 182'}]}}
```

## Contributing

Contributions to improve this module are welcome. You can contribute by:
* Reporting bugs
* Suggesting enhancements
* Sending pull requests with bug fixes or new features

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE](https://github.com/646e62/legal_citation_parser/blob/main/LICENSE) file for details.

