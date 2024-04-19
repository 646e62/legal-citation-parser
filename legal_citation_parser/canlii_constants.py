"""
Contains constants that map court names to their respective levels and jurisdictions.
"""

COURT_HIERARCHY_CRIMINAL = {
    "csc-scc": "federal appellate",
    "csc-scc-al": "federal appellate",
    "bcca": "provincial appellate",
    "bcsc": "superior",
    "bcpc": "provincial",
    "abca": "provincial appellate",
    "abkb": "superior",
    "abqb": "superior",
    "abpc": "provincial",
    "skca": "provincial appellate",
    "skkb": "superior",
    "skqb": "superior",
    "skpc": "provincial",
    "mbca": "provincial appellate",
    "mbkb": "superior",
    "mbqb": "superior",
    "mbpc": "provincial",
    "onca": "provincial appellate",
    "onsc": "superior",
    "oncj": "provincial",
    "qcca": "provincial appellate",
    "qccs": "superior",
    "qccq": "provincial",
    "nbca": "provincial appellate",
    "nbkb": "superior",
    "nkqb": "superior",
    "nbpc": "provincial",
    "nsca": "provincial appellate",
    "nssc": "superior",
    "nspc": "provincial",
    "pescad": "provincial appellate",
    "pesctd": "superior",
    "pepc": "provincial",
    "nlca": "provincial appellate",
    "nlsc": "superior",
    "nltd": "superior",
    "nlpc": "provincial",
    "ykca": "provincial appellate",
    "yksc": "superior",
    "yktc": "provincial",
    "ntca": "provincial appellate",
    "ntsc": "superior",
    "nttc": "provincial",
    "nuca": "provincial appellate",
    "nucj": "provincial",
    "yjcn": "provincial",
}

COURT_CODES = {
    "nlpc": {
        "jurisdiction": "nl",
        "name": {
            "en": "Provincial Court of Newfoundland and Labrador",
        },
        "url": {
            "en": "nlpc",
            "fr": "nlpc",
        },
        "court_id": ["nl pc"],
    },
    "nlpb": {
        "jurisdiction": "nl",
        "name": {
            "en": "Newfoundland and Labrador Pharmacy Board",
        },
        "url": {
            "en": "nlpb",
            "fr": "nlpb",
        },
        "court_id": ["nlpb"],
    },
    "qcopodq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des podiatres du Québec",
        },
        "url": {
            "en": "qcopodq",
            "fr": "qcopodq",
        },
        "court_id": ["qccdpod", "qc opodq"],
    },
    "qcamf": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Quebec Autorité des marchés financiers",
        },
        "url": {
            "en": "qcamf",
            "fr": "qcamf",
        },
        "court_id": ["qc amf"],
    },
    "abca": {
        "jurisdiction": "ab",
        "name": {
            "en": "Court of Appeal of Alberta",
            "fr": "Cour d'appel de l'Alberta",
        },
        "url": {
            "en": "abca",
            "fr": "abca",
        },
        "court_id": ["abca", "altascad", "ab ca"],
    },
    "bccnm": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia College of Nurses and Midwives",
        },
        "url": {
            "en": "bccnm",
            "fr": "bccnm",
        },
        "court_id": ["bccnm"],
    },
    "qccmmtq": {
        "jurisdiction": "qc",
        "name": {
            "en": "Corporation of Master Pipe-Mechanics of Québec",
            "fr": "Corporation des maîtres mécaniciens en tuyauterie du Québec",
        },
        "url": {
            "en": "qccmpmq",
            "fr": "qccmmtq",
        },
        "court_id": ["qc cmmtq"],
    },
    "nuwcat": {
        "jurisdiction": "nu",
        "name": {
            "en": "Northwest Territories and Nunavut Workers’ Compensation Appeals Tribunal",
            "fr": "Tribunal d'appel des accidents du travail des Territoires du Nord-Ouest et du Nunavut",
        },
        "url": {
            "en": "ntwcat",
            "fr": "ntwcat",
        },
        "court_id": ["nuwcat", "ntwcat", "nt wcat" "ntnuwcat"],
    },
    "skufc": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Unified Family Court",
        },
        "url": {
            "en": "skufc",
            "fr": "skufc",
        },
        "court_id": ["sk ufc"],
    },
    "nbsec": {
        "jurisdiction": "nb",
        "name": {
            "en": "Financial and Consumer Services Tribunal",
            "fr": "Tribunal des services financiers et des services aux consommateurs",
        },
        "url": {
            "en": "nbfcst",
            "fr": "nbfcst",
        },
        "court_id": ["nbfcst", "nbsecf"],
    },
    "oncdho": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Dental Hygienists of Ontario",
            "fr": "Ordre des hygiénistes dentaires de l'Ontario",
        },
        "url": {
            "en": "oncdho",
            "fr": "oncdho",
        },
        "court_id": ["oncdho"],
    },
    "qccpa": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des comptables professionnels agréés du Québec",
        },
        "url": {
            "en": "qccpa",
            "fr": "qccpa",
        },
        "court_id": ["qccdcpa", "qc cpa"],
    },
    "onhrt": {
        "jurisdiction": "on",
        "name": {
            "en": "Human Rights Tribunal of Ontario",
            "fr": "Tribunal des droits de la personne de l'Ontario",
        },
        "url": {
            "en": "onhrt",
            "fr": "onhrt",
        },
        "court_id": ["on hrt", "hrto"],
    },
    "qctt": {
        "jurisdiction": "qc",
        "name": {
            "en": "Labour Court",
            "fr": "Tribunal du travail",
        },
        "url": {
            "en": "qctt",
            "fr": "qctt",
        },
        "court_id": ["qc tt"],
    },
    "bchprb": {
        "jurisdiction": "bc",
        "name": {
            "en": "Health Professions Review Board of British Columbia",
        },
        "url": {
            "en": "bchprb",
            "fr": "bchprb",
        },
        "court_id": ["bchprb", "bc hprb"],
    },
    "nsawab": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Animal Welfare Appeal Board",
        },
        "url": {
            "en": "nsawab",
            "fr": "nsawab",
        },
        "court_id": ["nsawab"],
    },
    "qccdosfq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des sages-femmes du Québec",
        },
        "url": {
            "en": "qccdosfq",
            "fr": "qccdosfq",
        },
        "court_id": ["qccdsf", "qc cdosfq"],
    },
    "bcrmb": {
        "jurisdiction": "bc",
        "name": {
            "en": "Registrar of Mortgage Brokers",
        },
        "url": {
            "en": "bcrmb",
            "fr": "bcrmb",
        },
        "court_id": ["bcrmb"],
    },
    "bcest": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia Employment Standards Tribunal",
        },
        "url": {
            "en": "bcest",
            "fr": "bcest",
        },
        "court_id": ["bcest", "bc est"],
    },
    "qctp": {
        "jurisdiction": "qc",
        "name": {
            "en": "Professions Tribunal",
            "fr": "Tribunal des professions",
        },
        "url": {
            "en": "qctp",
            "fr": "qctp",
        },
        "court_id": ["qctp", "qc tp"],
    },
    "lsbc": {
        "jurisdiction": "bc",
        "name": {
            "en": "Law Society of British Columbia",
        },
        "url": {
            "en": "lsbc",
            "fr": "lsbc",
        },
        "court_id": ["lsbc", "ls bc"],
    },
    "qccdhj": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de la Chambre des huissiers de justice du Québec",
        },
        "url": {
            "en": "qccdhj",
            "fr": "qccdhj",
        },
        "court_id": ["qccdhj", "qc cdhj"],
    },
    "skipc": {
        "jurisdiction": "sk",
        "name": {
            "en": "Information and Privacy Commissioner",
        },
        "url": {
            "en": "skipc",
            "fr": "skipc",
        },
        "court_id": ["sk ipc"],
    },
    "abesu": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Employment Standards Appeals",
        },
        "url": {
            "en": "abesa",
            "fr": "abesa",
        },
        "court_id": ["abesab", "ab esa"],
    },
    "cmac-cacm": {
        "jurisdiction": "ca",
        "name": {
            "en": "Court Martial Appeal Court of Canada",
            "fr": "Cour d'appel de la cour martiale du Canada",
        },
        "url": {
            "en": "cmac",
            "fr": "cacm",
        },
        "court_id": ["cmac", "cacm"],
    },
    "oncswssw": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario College of Social Workers and Social Service Workers",
            "fr": "Ordre des travailleurs sociaux et des techniciens en travail social de l'Ontario",
        },
        "url": {
            "en": "oncswssw",
            "fr": "oncswssw",
        },
        "court_id": ["oncswssw"],
    },
    "qccdcrim": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des criminologues du Québec",
        },
        "url": {
            "en": "qccdcrim",
            "fr": "qccdcrim",
        },
        "court_id": ["qccdcrim", "qc cdcrim"],
    },
    "onbcc": {
        "jurisdiction": "on",
        "name": {
            "en": "Building Code Commission",
            "fr": "Commission du code du bâtiment",
        },
        "url": {
            "en": "onbcc",
            "fr": "onbcc",
        },
        "court_id": ["onbcc", "on bcc"],
    },
    "skac": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Assessment Commission",
        },
        "url": {
            "en": "skac",
            "fr": "skac",
        },
        "court_id": ["sk ac"],
    },
    "nuca": {
        "jurisdiction": "nu",
        "name": {
            "en": "Court of Appeal of Nunavut",
            "fr": "Cour d'appel du Nunavut",
        },
        "url": {
            "en": "nuca",
            "fr": "nuca",
        },
        "court_id": ["nuca", "nu ca"],
    },
    "bccps": {
        "jurisdiction": "bc",
        "name": {
            "en": "College of Physicians and Surgeons of British Columbia",
        },
        "url": {
            "en": "bccps",
            "fr": "bccps",
        },
        "court_id": ["bc cps"],
    },
    "abrtdrs": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Residential Tenancy Dispute Resolution Service",
        },
        "url": {
            "en": "abrtdrs",
            "fr": "abrtdrs",
        },
        "court_id": ["abrtdrs"],
    },
    "abcpa": {
        "jurisdiction": "ab",
        "name": {
            "en": "Chartered Professional Accountants of Alberta",
        },
        "url": {
            "en": "abcpa",
            "fr": "abcpa",
        },
        "court_id": ["abcpa"],
    },
    "onsc": {
        "jurisdiction": "on",
        "name": {
            "en": "Superior Court of Justice",
            "fr": "Cour supérieure de justice",
        },
        "url": {
            "en": "onsc",
            "fr": "onsc",
        },
        "court_id": ["onsc", "on sc"],
    },
    "nlhrc": {
        "jurisdiction": "nl",
        "name": {
            "en": "Newfoundland and Labrador Human Rights Commission",
        },
        "url": {
            "en": "nlhrc",
            "fr": "nlhrc",
        },
        "court_id": ["nl hrc"],
    },
    "nucj": {
        "jurisdiction": "nu",
        "name": {
            "en": "Nunavut Court of Justice",
            "fr": "Cour de justice du Nunavut",
        },
        "url": {
            "en": "nucj",
            "fr": "nucj",
        },
        "court_id": ["nucj", "nu cj"],
    },
    "onsec": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Securities Commission",
            "fr": "Commission des valeurs mobilières de l'Ontario",
        },
        "url": {
            "en": "onsec",
            "fr": "oncvm",
        },
        "court_id": ["on sec", "on cvm"],
    },
    "peipc": {
        "jurisdiction": "pe",
        "name": {
            "en": "Information and Privacy Commissioner",
        },
        "url": {
            "en": "peipc",
            "fr": "peipc",
        },
        "court_id": ["pe ipc"],
    },
    "nssirt": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Serious Incident Response Team",
        },
        "url": {
            "en": "nssirt",
            "fr": "nssirt",
        },
        "court_id": ["ns sirt"],
    },
    "abcpt": {
        "jurisdiction": "ab",
        "name": {
            "en": "College of Physiotherapists of Alberta",
        },
        "url": {
            "en": "abcpt",
            "fr": "abcpt",
        },
        "court_id": ["abcpt", "abpaca"],
    },
    "onrc": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Racing Commission",
            "fr": "Commission des courses de l'Ontario",
        },
        "url": {
            "en": "onrc",
            "fr": "onrc",
        },
        "court_id": ["on rc"],
    },
    "nbrea": {
        "jurisdiction": "nb",
        "name": {
            "en": "New Brunswick Real Estate Association",
        },
        "url": {
            "en": "nbrea",
            "fr": "nbrea",
        },
        "court_id": ["nbrea"],
    },
    "abci": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Commission of Inquiry",
        },
        "url": {
            "en": "abci",
            "fr": "abci",
        },
        "court_id": ["ab ci"],
    },
    "cm": {
        "jurisdiction": "ca",
        "name": {
            "en": "Courts Martial",
            "fr": "Cours martiales",
        },
        "url": {
            "en": "cm",
            "fr": "cm",
        },
        "court_id": ["cm" "ca cm"],
    },
    "onset": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Special Education  (English) Tribunal",
            "fr": "Tribunal (Français) de l'enfance en difficulté de l'Ontario",
        },
        "url": {
            "en": "onset",
            "fr": "onset",
        },
        "court_id": ["onset", "onted"],
    },
    "qcrmaaq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Régie des marchés agricoles et alimentaires du Québec",
        },
        "url": {
            "en": "qcrmaaq",
            "fr": "qcrmaaq",
        },
        "court_id": ["qcrmaaq"],
    },
    "qcoeq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des ergothérapeutes du Québec",
        },
        "url": {
            "en": "qcoeq",
            "fr": "qcoeq",
        },
        "court_id": ["qc oeq", "qccderg"],
    },
    "bcca": {
        "jurisdiction": "bc",
        "name": {
            "en": "Court of Appeal for British Columbia",
            "fr": "Cour d'appel de la Colombie-Britannique",
        },
        "url": {
            "en": "bcca",
            "fr": "bcca",
        },
        "court_id": ["bcca", "bc ca"],
    },
    "qcbdrvm": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Tribunal administratif des marchés financiers",
        },
        "url": {
            "en": "qctmf",
            "fr": "qctmf",
        },
        "court_id": ["qctmf", "qc tmf" "qcbdr", "qcbdrvm"],
    },
    "eptc": {
        "jurisdiction": "ca",
        "name": {
            "en": "Environmental Protection Tribunal of Canada",
            "fr": "Tribunal de la protection de l’environnement du Canada",
        },
        "url": {
            "en": "eptc",
            "fr": "tpec",
        },
        "court_id": ["eptc", "tpec"],
    },
    "sksec": {
        "jurisdiction": "sk",
        "name": {
            "en": "Financial and Consumer Affairs Authority of Saskatchewan",
        },
        "url": {
            "en": "sksec",
            "fr": "sksec",
        },
        "court_id": ["sk fcaa"],
    },
    "pslreb": {
        "jurisdiction": "ca",
        "name": {
            "en": "Federal Public Sector Labour Relations and Employment Board",
            "fr": "Commission des relations de travail et de l’emploi dans le secteur public fédéral",
        },
        "url": {
            "en": "pslreb",
            "fr": "crtefp",
        },
        "court_id": ["fpslreb", "pslreb", "crtespf", "crtefp"],
    },
    "mbca": {
        "jurisdiction": "mb",
        "name": {
            "en": "Court of Appeal of Manitoba",
            "fr": "Cour d'appel du Manitoba",
        },
        "url": {
            "en": "mbca",
            "fr": "mbca",
        },
        "court_id": ["mbca", "mb ca"],
    },
    "skca": {
        "jurisdiction": "sk",
        "name": {
            "en": "Court of Appeal for Saskatchewan",
            "fr": "Cour d'appel de la Saskatchewan",
        },
        "url": {
            "en": "skca",
            "fr": "skca",
        },
        "court_id": ["skca", "sk ca"],
    },
    "qccdnq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de la Chambre des notaires du Québec",
        },
        "url": {
            "en": "qccdnq",
            "fr": "qccdnq",
        },
        "court_id": ["qc cdnq", "qccdnot"],
    },
    "ntwcat": {
        "jurisdiction": "nt",
        "name": {
            "en": "Northwest Territories and Nunavut Workers’ Compensation Appeals Tribunal",
            "fr": "Tribunal d’appel des accidents du travail des Territoires du Nord-Ouest et du Nunavut",
        },
        "url": {
            "en": "ntwcat",
            "fr": "ntwcat",
        },
        "court_id": ["ntwcat", "nt wcat", "ntnuwcat", "nuwcat"],
    },
    "onombud": {
        "jurisdiction": "on",
        "name": {
            "en": "Office of the Ombudsman of Ontario",
            "fr": "Bureau de l’Ombudsman de l’Ontario",
        },
        "url": {
            "en": "onombud",
            "fr": "onombud",
        },
        "court_id": ["onombud"],
    },
    "qcochq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des chimistes du Québec",
        },
        "url": {
            "en": "qcochq",
            "fr": "qcochq",
        },
        "court_id": [
            "qcochq",
            "qccdchim",
        ],
    },
    "ntca": {
        "jurisdiction": "nt",
        "name": {
            "en": "Court of Appeal for the Northwest Territories",
            "fr": "Cour d'appel des Territoires du Nord-Ouest",
        },
        "url": {
            "en": "ntca",
            "fr": "ntca",
        },
        "court_id": ["nwtca", "nwt ca"],
    },
    "onscsm": {
        "jurisdiction": "on",
        "name": {
            "en": "Small Claims Court",
            "fr": "Cour des petites créances",
        },
        "url": {
            "en": "onscsm",
            "fr": "onscsm",
        },
        "court_id": ["on scsm"],
    },
    "qcctq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission des transports du Québec",
        },
        "url": {
            "en": "qcctq",
            "fr": "qcctq",
        },
        "court_id": ["qcctq"],
    },
    "abesdab": {
        "jurisdiction": "ab",
        "name": {
            "en": "Edmonton Subdivision and Development Appeal Board",
        },
        "url": {
            "en": "abesdab",
            "fr": "abesdab",
        },
        "court_id": ["abesdab"],
    },
    "abwcac": {
        "jurisdiction": "ab",
        "name": {
            "en": "Appeals Commission for Alberta Workers' Compensation",
        },
        "url": {
            "en": "abwcac",
            "fr": "abwcac",
        },
        "court_id": ["ab wcac"],
    },
    "onoct": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario College of Teachers",
            "fr": "Ordre des enseignantes et des enseignants de l'Ontario",
        },
        "url": {
            "en": "onoct",
            "fr": "onoct",
        },
        "court_id": ["onoct"],
    },
    "csc-scc-al": {
        "jurisdiction": "ca",
        "name": {
            "en": "Supreme Court of Canada - Applications for Leave",
            "fr": "Cour suprême du Canada - Demandes d'autorisation",
        },
        "url": {
            "en": "scc-l",
            "fr": "csc-a",
        },
        "court_id": ["scc", "csc"],
    },
    "qcolf": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Office de la langue française",
        },
        "url": {
            "en": "qcolf",
            "fr": "qcolf",
        },
        "court_id": ["qcolf"],
    },
    "mbsec": {
        "jurisdiction": "mb",
        "name": {
            "en": "Manitoba Securities Commission",
            "fr": "Commission des valeurs mobilières du Manitoba",
        },
        "url": {
            "en": "mbsec",
            "fr": "mbcvm",
        },
        "court_id": ["mb sec", "mb cvm"],
    },
    "onst": {
        "jurisdiction": "on",
        "name": {
            "en": "Skilled Trades Ontario",
            "fr": "Métiers spécialisés Ontario",
        },
        "url": {
            "en": "onst",
            "fr": "onms",
        },
        "court_id": ["onct"],
    },
    "qccdccoq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline des Conseillers et conseillères d'orientation du Québec",
        },
        "url": {
            "en": "qccdccoq",
            "fr": "qccdccoq",
        },
        "court_id": ["qc cdccoq", "qccdco"],
    },
    "onfsc": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Fire Safety Commission",
            "fr": "Commission de la sécurité-incendie de l'Ontario",
        },
        "url": {
            "en": "onfsc",
            "fr": "oncsi",
        },
        "court_id": ["onfsc", "oncsi", "on fsc"],
    },
    "sst-tss": {
        "jurisdiction": "ca",
        "name": {
            "en": "Social Security Tribunal of Canada",
            "fr": "Tribunal de la sécurité sociale du Canada",
        },
        "url": {
            "en": "sst",
            "fr": "tss",
        },
        "court_id": ["sst", "sstad", "tss", "tssda"],
    },
    "onhparb": {
        "jurisdiction": "on",
        "name": {
            "en": "Health Professions Appeal and Review Board",
            "fr": "Commission d'appel et de révision des professions de la santé",
        },
        "url": {
            "en": "onhparb",
            "fr": "oncarps",
        },
        "court_id": ["on carps", "on hparb"],
    },
    "sklrb": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Labour Relations Board",
        },
        "url": {
            "en": "sklrb",
            "fr": "sklrb",
        },
        "court_id": ["sk lrb"],
    },
    "qccse": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil des services essentiels",
        },
        "url": {
            "en": "qccse",
            "fr": "qccse",
        },
        "court_id": ["qc cse"],
    },
    "mbhrc": {
        "jurisdiction": "mb",
        "name": {
            "en": "Manitoba Human Rights Commission",
            "fr": "Commission des droits de la personne du Manitoba",
        },
        "url": {
            "en": "mbhrc",
            "fr": "mbhrc",
        },
        "court_id": ["mbhr", "mb hrc"],
    },
    "qccsj": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission des services juridiques",
        },
        "url": {
            "en": "qccsj",
            "fr": "qccsj",
        },
        "court_id": ["qccsj"],
    },
    "nsca": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Court of Appeal",
        },
        "url": {
            "en": "nsca",
            "fr": "nsca",
        },
        "court_id": ["nsca", "ns ca"],
    },
    "yksm": {
        "jurisdiction": "yk",
        "name": {
            "en": "Small Claims Court of the Yukon",
            "fr": "Cour des petites créances du Yukon",
        },
        "url": {
            "en": "yksm",
            "fr": "yksm",
        },
        "court_id": ["yksm"],
    },
    "pesctd": {
        "jurisdiction": "pe",
        "name": {
            "en": "Supreme Court of Prince Edward Island",
        },
        "url": {
            "en": "pesctd",
            "fr": "pesctd",
        },
        "court_id": ["pesctd", "pe sctd", "pesc"],
    },
    "yksc": {
        "jurisdiction": "yk",
        "name": {
            "en": "Supreme Court  of Yukon",
            "fr": "Cour suprême du Yukon",
        },
        "url": {
            "en": "yksc",
            "fr": "yksc",
        },
        "court_id": ["yksc"],
    },
    "skdc": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan District Court",
        },
        "url": {
            "en": "skdc",
            "fr": "skdc",
        },
        "court_id": ["skdc"],
    },
    "nsbs": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Barristers' Society Hearing Panel",
        },
        "url": {
            "en": "nsbs",
            "fr": "nsbs",
        },
        "court_id": ["nsbs"],
    },
    "abelarb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Edmonton Local Assessment Review Board",
        },
        "url": {
            "en": "abelarb",
            "fr": "abelarb",
        },
        "court_id": ["abelarb"],
    },
    "skcp": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan College of Pharmacy Professionals",
        },
        "url": {
            "en": "skcppdc",
            "fr": "skcppdc",
        },
        "court_id": ["skcppdc"],
    },
    "onagc": {
        "jurisdiction": "on",
        "name": {
            "en": "Alcohol and Gaming Commission of Ontario",
            "fr": "Commission des alcools et des jeux de l'Ontario",
        },
        "url": {
            "en": "onagc",
            "fr": "onagc",
        },
        "court_id": ["on agc"],
    },
    "sklss": {
        "jurisdiction": "sk",
        "name": {
            "en": "Law Society of Saskatchewan",
        },
        "url": {
            "en": "sklss",
            "fr": "sklss",
        },
        "court_id": ["sklss", "lss", "sk lss"],
    },
    "qccrt": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission des relations du travail",
        },
        "url": {
            "en": "qccrt",
            "fr": "qccrt",
        },
        "court_id": ["qccrt", "qc crt"],
    },
    "bcfst": {
        "jurisdiction": "bc",
        "name": {
            "en": "Financial Services Tribunal",
        },
        "url": {
            "en": "bcfst",
            "fr": "bcfst",
        },
        "court_id": ["bcfst"],
    },
    "ongsb": {
        "jurisdiction": "on",
        "name": {
            "en": "Grievance Settlement Board",
            "fr": "Commission de règlement des griefs",
        },
        "url": {
            "en": "ongsb",
            "fr": "oncrg",
        },
        "court_id": ["on gsb", "on crg"],
    },
    "onwsib": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Workplace Safety and Insurance Board",
            "fr": "Commission de la sécurité professionnelle et de l'assurance contre les accidents du travail de l'Ontario",
        },
        "url": {
            "en": "onwsib",
            "fr": "oncspaat",
        },
        "court_id": ["on wsib", "on cspaat"],
    },
    "nsprb": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Police Review Board",
        },
        "url": {
            "en": "nsprb",
            "fr": "nsprb",
        },
        "court_id": ["ns prb"],
    },
    "qccalp": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission d'appel en matière de lésions professionnelles du Québec",
        },
        "url": {
            "en": "qccalp",
            "fr": "qccalp",
        },
        "court_id": ["qc calp"],
    },
    "nbapab": {
        "jurisdiction": "nb",
        "name": {
            "en": "New Brunswick Assessment and Planning Appeal Board",
            "fr": "Commission d'appel en matière d'évaluation et d'urbanisme du Nouveau Brunswick",
        },
        "url": {
            "en": "nbapab",
            "fr": "nbcaeu",
        },
        "court_id": ["nbapab", "nbcaeu", "nb caeu", "nb apab"],
    },
    "ciro-ocri": {
        "jurisdiction": "ca",
        "name": {
            "en": "Canadian Investment Regulatory Organization",
            "fr": "Organisme canadien de réglementation des investissements",
        },
        "url": {
            "en": "ciro",
            "fr": "ocri",
        },
        "court_id": ["ciro", "ocri"],
    },
    "oncece": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario College of Early Childhood Educators",
            "on": "Ordre des éducatrices et des educateurs de la petite enfance de l'Ontario",
        },
        "url": {
            "en": "oncece",
            "fr": "oncece",
        },
        "court_id": ["onoepe", "oncece"],
    },
    "nswcat": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Workers' Compensation Appeals Tribunal",
        },
        "url": {
            "en": "nswcat",
            "fr": "nswcat",
        },
        "court_id": ["ns wcat"],
    },
    "bcsfi": {
        "jurisdiction": "bc",
        "name": {
            "en": "Superintendent of Financial Institutions",
        },
        "url": {
            "en": "bcsfi",
            "fr": "bcsfi",
        },
        "court_id": ["bcsfi"],
    },
    "oncfsrb": {
        "jurisdiction": "on",
        "name": {
            "en": "Child and Family Services Review Board",
            "fr": "Commission de révision des services à l'enfance et à la famille",
        },
        "url": {
            "en": "oncfsrb",
            "fr": "oncrsef",
        },
        "court_id": ["cfsrb"],
    },
    "pescad": {
        "jurisdiction": "pe",
        "name": {
            "en": "Prince Edward Island Court of Appeal",
        },
        "url": {
            "en": "pescad",
            "fr": "pescad",
        },
        "court_id": ["pescad", "pe scad", "peca", "pe ca"],
    },
    "absec": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Securities Commission",
        },
        "url": {
            "en": "absec",
            "fr": "absec",
        },
        "court_id": ["abasc", "ab sec"],
    },
    "oncpd": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Psychologists of Ontario",
            "fr": "Ordre des psychologues de l’Ontario",
        },
        "url": {
            "en": "oncpd",
            "fr": "oncpd",
        },
        "court_id": ["oncpd"],
    },
    "oncpc": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Civilian Police Commission",
            "fr": "Commission civile de l'Ontario sur la police",
        },
        "url": {
            "en": "oncpc",
            "fr": "oncpc",
        },
        "court_id": ["oncpc", "on cpc"],
    },
    "ntllb": {
        "jurisdiction": "nt",
        "name": {
            "en": "Northwest Territories Liquor Licensing Board",
        },
        "url": {
            "en": "ntllb",
            "fr": "ntllb",
        },
        "court_id": ["ntllb"],
    },
    "oncpa": {
        "jurisdiction": "on",
        "name": {
            "en": "Chartered Professional Accountants of Ontario",
            "fr": "Comptables professionnels agréés de l’Ontario",
        },
        "url": {
            "en": "oncpa",
            "fr": "oncpa",
        },
        "court_id": ["oncpa"],
    },
    "nsfoipop": {
        "jurisdiction": "ns",
        "name": {
            "en": "Office of the Information and Privacy Commissioner for Nova Scotia",
        },
        "url": {
            "en": "nsfoipop",
            "fr": "nsfoipop",
        },
        "court_id": [
            "nsoipc",
            "ns foipop",
        ],
    },
    "qcotmq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des technologistes médicaux du Québec",
        },
        "url": {
            "en": "qcotmq",
            "fr": "qcotmq",
        },
        "court_id": ["qc otmq"],
    },
    "nbca": {
        "jurisdiction": "nb",
        "name": {
            "en": "Court of Appeal of New Brunswick",
            "fr": "Cour d'appel du Nouveau-Brunswick",
        },
        "url": {
            "en": "nbca",
            "fr": "nbca",
        },
        "court_id": ["nbca", "nb ca"],
    },
    "onpprb": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Physician Payment Review Board",
            "fr": "Commission de révision des paiements effectués aux médecins de l'Ontario",
        },
        "url": {
            "en": "onpprb",
            "fr": "onpprb",
        },
        "court_id": ["on pprb"],
    },
    "skatmpa": {
        "jurisdiction": "sk",
        "name": {
            "en": "Appeal Tribunal under the Medical Profession Act",
        },
        "url": {
            "en": "skatmpa",
            "fr": "skatmpa",
        },
        "court_id": ["sk atmpa"],
    },
    "oncps": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Physicians and Surgeons Discipline Tribunal",
            "fr": "Tribunal de discipline des médecins et chirurgiens de l’Ontario",
        },
        "url": {
            "en": "onpsdt",
            "fr": "onpsdt",
        },
        "court_id": ["oncps", "onpsdt", "oncpsd", "on psdt"],
    },
    "oncpo": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Physiotherapists of Ontario",
        },
        "url": {
            "en": "oncpo",
            "fr": "oncpo",
        },
        "court_id": ["oncpo", "on cpo"],
    },
    "onlat": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Licence Appeal Tribunal",
            "fr": "Tribunal d’appel en matière de permis de l'Ontario",
        },
        "url": {
            "en": "onlat",
            "fr": "onlat",
        },
        "court_id": ["on lat"],
    },
    "qcotimro": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des technologues en imagerie médicale et en radio-oncologie du Québec",
        },
        "url": {
            "en": "qcotimro",
            "fr": "qcotimro",
        },
        "court_id": ["qc otimro", "qccdtimroem"],
    },
    "qcoagq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des arpenteurs-géomètres du Québec",
        },
        "url": {
            "en": "qcoagq",
            "fr": "qcoagq",
        },
        "court_id": ["qc oagq", "qccdag"],
    },
    "cirb": {
        "jurisdiction": "ca",
        "name": {
            "en": "Canada Industrial Relations Board",
            "fr": "Conseil canadien des relations industrielles",
        },
        "url": {
            "en": "cirb",
            "fr": "ccri",
        },
        "court_id": ["cirb", "ccri"],
    },
    "yktc": {
        "jurisdiction": "yk",
        "name": {
            "en": "Territorial Court of Yukon",
            "fr": "Cour territoriale du Yukon",
        },
        "url": {
            "en": "yktc",
            "fr": "yktc",
        },
        "court_id": ["yktc", "yk tc", "ykyc", "yk yc", "yttc", "yt tc"],
    },
    "qcopq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des psychologues du Québec",
        },
        "url": {
            "en": "qcopq",
            "fr": "qcopq",
        },
        "court_id": ["qc opq", "qccdpsy"],
    },
    "qcopdq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Ordre professionnel des diététistes du Québec",
        },
        "url": {
            "en": "qcopdq",
            "fr": "qcopdq",
        },
        "court_id": ["qc opdq", "qccddtp"],
    },
    "abcpsdc": {
        "jurisdiction": "ab",
        "name": {
            "en": "College of Physicians and Surgeons Discipline Committee",
        },
        "url": {
            "en": "abcpsdc",
            "fr": "abcpsdc",
        },
        "court_id": ["ab cpsdc"],
    },
    "bcrec": {
        "jurisdiction": "bc",
        "name": {
            "en": "Real Estate Council of British Columbia",
        },
        "url": {
            "en": "bcrec",
            "fr": "bcrec",
        },
        "court_id": ["bc rec"],
    },
    "nbfc": {
        "jurisdiction": "nb",
        "name": {
            "en": "Financial and Consumer Services Commission",
            "fr": "Commission des services financiers et des services aux consommateurs",
        },
        "url": {
            "en": "nbfcsc",
            "fr": "nbfcsc",
        },
        "court_id": ["nbfcsc"],
    },
    "oncmt": {
        "jurisdiction": "on",
        "name": {
            "en": "Capital Markets Tribunal",
            "fr": "Tribunal des marchés financiers",
        },
        "url": {
            "en": "oncmt",
            "fr": "ontmf",
        },
        "court_id": ["oncmt", "ontmf", "onsec"],
    },
    "abls": {
        "jurisdiction": "ab",
        "name": {
            "en": "Law Society of Alberta",
        },
        "url": {
            "en": "abls",
            "fr": "abls",
        },
        "court_id": ["abls", "lsa"],
    },
    "onfst": {
        "jurisdiction": "on",
        "name": {
            "en": "Financial Services Tribunal",
            "fr": "Tribunal des services financiers",
        },
        "url": {
            "en": "onfst",
            "fr": "onfst",
        },
        "court_id": ["onfst", "on fst"],
    },
    "abecarb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Edmonton Composite Assessment Review Board",
        },
        "url": {
            "en": "abecarb",
            "fr": "abecarb",
        },
        "court_id": ["abecarb"],
    },
    "bclcrb": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia Liquor and Cannabis Regulation Branch",
        },
        "url": {
            "en": "bclcrb",
            "fr": "bclcrb",
        },
        "court_id": ["bclcrb", "bc lcrb"],
    },
    "chrt": {
        "jurisdiction": "ca",
        "name": {
            "en": "Canadian Human Rights Tribunal",
            "fr": "Tribunal canadien des droits de la personne",
        },
        "url": {
            "en": "chrt",
            "fr": "tcdp",
        },
        "court_id": ["chrt", "tcdp"],
    },
    "nula": {
        "jurisdiction": "nu",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "nula",
            "fr": "nula",
        },
        "court_id": ["nu la"],
    },
    "yttlrb": {
        "jurisdiction": "yk",
        "name": {
            "en": "Yukon Teachers Labour Relations Board",
        },
        "url": {
            "en": "yttlrb",
            "fr": "yttlrb",
        },
        "court_id": ["yt tlrb"],
    },
    "ontlab": {
        "jurisdiction": "on",
        "name": {
            "en": "Toronto Local Appeal Body",
        },
        "url": {
            "en": "ontlab",
            "fr": "ontlab",
        },
        "court_id": ["ontlab"],
    },
    "qcodlq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des denturologistes du Québec",
        },
        "url": {
            "en": "qcodlq",
            "fr": "qcodlq",
        },
        "court_id": ["qc odlq", "qccddd"],
    },
    "bcla": {
        "jurisdiction": "bc",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "bcla",
            "fr": "bcla",
        },
        "court_id": ["bc la"],
    },
    "qcooq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des optométristes du Québec",
        },
        "url": {
            "en": "qcooq",
            "fr": "qcooq",
        },
        "court_id": ["qccdooq", "qc ooq"],
    },
    "qcooaq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des orthophonistes et audiologistes du Québec",
        },
        "url": {
            "en": "qcooaq",
            "fr": "qcooaq",
        },
        "court_id": ["qc ooaq", "qccdoaq"],
    },
    "ytpslrb": {
        "jurisdiction": "yk",
        "name": {
            "en": "Yukon Public Service Labour Relations Board",
        },
        "url": {
            "en": "ytpslrb",
            "fr": "ytpslrb",
        },
        "court_id": ["yt pslrb"],
    },
    "bchrt": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia Human Rights Tribunal",
        },
        "url": {
            "en": "bchrt",
            "fr": "bchrt",
        },
        "court_id": ["bchrt", "bc hrt"],
    },
    "nbcph": {
        "jurisdiction": "nb",
        "name": {
            "en": "New Brunswick College of Pharmacists",
            "fr": "Ordre des pharmaciens du Nouveau-Brunswick",
        },
        "url": {
            "en": "nbcph",
            "fr": "nbcph",
        },
        "court_id": ["nboph"],
    },
    "abhrc": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Human Rights Commission",
        },
        "url": {
            "en": "abhrc",
            "fr": "abhrc",
        },
        "court_id": ["ahrc", "ab hrc"],
    },
    "cact": {
        "jurisdiction": "ca",
        "name": {
            "en": "Competition Tribunal",
            "fr": "Tribunal de la concurrence",
        },
        "url": {
            "en": "cact",
            "fr": "cact",
        },
        "court_id": ["cact", "ct", "tc"],
    },
    "oncmto": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Massage Therapists of Ontario",
            "fr": "Ordre des massothérapeutes de l’Ontario",
        },
        "url": {
            "en": "oncmto",
            "fr": "oncmto",
        },
        "court_id": ["oncmto"],
    },
    "cacp": {
        "jurisdiction": "ca",
        "name": {
            "en": "Commissioner of Patents",
            "fr": "Commissaire aux brevets",
        },
        "url": {
            "en": "cacp",
            "fr": "cacb",
        },
        "court_id": ["cacp", "ca cp", "cacb", "ca cb"],
    },
    "sopf": {
        "jurisdiction": "ca",
        "name": {
            "en": "Ship-source Oil Pollution Fund",
            "fr": "Caisse d'indemnisation des dommages dus à la pollution par les hydrocarbures causée par les navires",
        },
        "url": {
            "en": "sopf",
            "fr": "sopf",
        },
        "court_id": ["cidphn"],
    },
    "onert": {
        "jurisdiction": "on",
        "name": {
            "en": "Environmental Review Tribunal",
            "fr": "Tribunal de l'environnement de l'Ontario",
        },
        "url": {
            "en": "onert",
            "fr": "onte",
        },
        "court_id": ["on ert", "on te"],
    },
    "skaia": {
        "jurisdiction": "sk",
        "name": {
            "en": "Automobile Injury Appeal Commission",
        },
        "url": {
            "en": "skaia",
            "fr": "skaia",
        },
        "court_id": ["skaia"],
    },
    "nlcps": {
        "jurisdiction": "nl",
        "name": {
            "en": "College of Physicians and Surgeons of Newfoundland and Labrador",
        },
        "url": {
            "en": "nlcps",
            "fr": "nlcps",
        },
        "court_id": ["nlcps"],
    },
    "caci": {
        "jurisdiction": "ca",
        "name": {
            "en": "Federal Commission of Inquiry",
            "fr": "Commission d'enquête fédérale",
        },
        "url": {
            "en": "caci",
            "fr": "cace",
        },
        "court_id": ["ca ci", "ca ce"],
    },
    "oncno": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Nurses of Ontario Discipline Committee",
            "fr": "Comité de discipline de l’Ordre des infirmières et infirmiers de l’Ontario",
        },
        "url": {
            "en": "oncno",
            "fr": "oncno",
        },
        "court_id": ["on cno"],
    },
    "cisr": {
        "jurisdiction": "ca",
        "name": {
            "en": "Immigration and Refugee Board of Canada",
            "fr": "Commission de l'immigration et du statut de réfugié du Canada",
        },
        "url": {
            "en": "irb",
            "fr": "cisr",
        },
        "court_id": ["ca cisr", "ca irb"],
    },
    "qccvm": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission des valeurs mobilières du Québec",
        },
        "url": {
            "en": "qccvm",
            "fr": "qccvm",
        },
        "court_id": ["qc cvm"],
    },
    "onfscdrs": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Financial Services Commission - Dispute Resolution Services",
            "fr": "Commission des services financiers de l'Ontario - Groupe de règlement des différends",
        },
        "url": {
            "en": "onfscdrs",
            "fr": "onfscdrs",
        },
        "court_id": ["onfscdrs", "onicdrg"],
    },
    "nsfc": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Family Court",
        },
        "url": {
            "en": "nsfc",
            "fr": "nsfc",
        },
        "court_id": ["nsfc", "ns fc"],
    },
    "qccptaq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission de protection du territoire agricole du Québec",
        },
        "url": {
            "en": "qccptaq",
            "fr": "qccptaq",
        },
        "court_id": ["qc cptaq"],
    },
    "qccdrhri": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des conseillers en ressources humaines et en relations industrielles agrées du Québec",
        },
        "url": {"en": "qccdrhri"},
        "court_id": ["qccdcrhri", "qc cdrhri"],
    },
    "sksmb": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Municipal Board",
        },
        "url": {
            "en": "skmb",
            "fr": "skmb",
        },
        "court_id": ["skmb"],
    },
    "ablprt": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Land and Property Rights Tribunal",
        },
        "url": {
            "en": "ablprt",
            "fr": "ablprt",
        },
        "court_id": ["ablprt"],
    },
    "ntla": {
        "jurisdiction": "nt",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "ntla",
            "fr": "ntla",
        },
        "court_id": ["nt la"],
    },
    "pec-ces": {
        "jurisdiction": "ca",
        "name": {
            "en": "Pay Equity Commissioner",
            "fr": "Commissaire à l’équité salariale",
        },
        "url": {
            "en": "pec",
            "fr": "ces",
        },
        "court_id": ["pec", "ces"],
    },
    "qcracj": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Régie des alcools des courses et des jeux",
        },
        "url": {
            "en": "qcracj",
            "fr": "qcracj",
        },
        "court_id": ["qcracj", "qc racj"],
    },
    "qccsst": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission de la santé et de la sécurité du travail",
        },
        "url": {
            "en": "qccsst",
            "fr": "qccsst",
        },
        "court_id": ["qccsst", "qc csst"],
    },
    "qccnesst": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission des normes, de l’équité, de la santé et de la sécurité du travail",
        },
        "url": {"en": "qccnesst"},
        "court_id": ["qccnesst"],
    },
    "onape": {
        "jurisdiction": "on",
        "name": {
            "en": "Association of Professional Engineers of Ontario",
        },
        "url": {
            "en": "onape",
            "fr": "onape",
        },
        "court_id": ["onape"],
    },
    "onconrb": {
        "jurisdiction": "on",
        "name": {
            "en": "Conservation Review Board",
            "fr": "Commission des biens culturels",
        },
        "url": {
            "en": "onconrb",
            "fr": "onconrb",
        },
        "court_id": ["on conrb"],
    },
    "qcouq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des urbanistes du Québec",
        },
        "url": {
            "en": "qcouq",
            "fr": "qcouq",
        },
        "court_id": ["qc ouq"],
    },
    "qccdottdq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des techniciens et techniciennes dentaires du Québec",
        },
        "url": {
            "en": "qccdottdq",
            "fr": "qccdottdq",
        },
        "court_id": ["qc cdottdq"],
    },
    "abplab": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Public Lands Appeal Board",
        },
        "url": {
            "en": "abplab",
            "fr": "abplab",
        },
        "court_id": ["abplab", "ab plab"],
    },
    "qcopiq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Ordre professionnel des inhalothérapeutes du Québec",
        },
        "url": {
            "en": "qcopiq",
            "fr": "qcopiq",
        },
        "court_id": ["qc opiq"],
    },
    "qctacarra": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Tribunal d'arbitrage (RQ and CARRA)",
        },
        "url": {
            "en": "qcta",
            "fr": "qcta",
        },
        "court_id": ["qcta", "qc ta"],
    },
    "bcipc": {
        "jurisdiction": "bc",
        "name": {
            "en": "Information and Privacy Commissioner",
        },
        "url": {
            "en": "bcipc",
            "fr": "bcipc",
        },
        "court_id": ["bcipc", "bc icp"],
    },
    "ntyjc": {
        "jurisdiction": "nt",
        "name": {
            "en": "Youth Justice Court",
        },
        "url": {"en": "ntyjc"},
        "court_id": ["nwttc", "nwtsc"],
    },
    "tatc": {
        "jurisdiction": "ca",
        "name": {
            "en": "Transportation Appeal Tribunal of Canada",
            "fr": "Tribunal d'appel des transports du Canada",
        },
        "url": {
            "en": "tatc",
            "fr": "tatc",
        },
        "court_id": ["tatcf", "tatce", "ca tat"],
    },
    "nslst": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Labour Standards Tribunal",
        },
        "url": {
            "en": "nslst",
            "fr": "nslst",
        },
        "court_id": ["nslst", "ns lst"],
    },
    "nsohsap": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Occupational Health and Safety Appeal Panel",
        },
        "url": {
            "en": "nsohsap",
            "fr": "nsohsap",
        },
        "court_id": ["nsohsap", "ns ohsap"],
    },
    "qccdchad": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Comité de discipline de la Chambre de l'assurance de dommages",
        },
        "url": {
            "en": "qccdchad",
            "fr": "qccdchad",
        },
        "court_id": ["qc cdchad"],
    },
    "nuls": {
        "jurisdiction": "nu",
        "name": {
            "en": "Law Society of Nunavut",
            "fr": "Barreau du Nunavut",
        },
        "url": {
            "en": "nuls",
            "fr": "nuls",
        },
        "court_id": ["nuls"],
    },
    "skrec": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Real Estate Commission",
        },
        "url": {
            "en": "skrec",
            "fr": "skrec",
        },
        "court_id": ["skrec"],
    },
    "bccds": {
        "jurisdiction": "bc",
        "name": {
            "en": "College of Dental Surgeons of British Columbia",
        },
        "url": {
            "en": "bccds",
            "fr": "bccds",
        },
        "court_id": ["bc cds"],
    },
    "qcotpq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des technologues professionnels du Québec",
        },
        "url": {
            "en": "qcotpq",
            "fr": "qcotpq",
        },
        "court_id": ["qccdtp", "qc otpq"],
    },
    "qcca": {
        "jurisdiction": "qc",
        "name": {
            "en": "Court of Appeal of Quebec",
            "fr": "Cour d'appel du Québec",
        },
        "url": {
            "en": "qcca",
            "fr": "qcca",
        },
        "court_id": ["qcca", "qc ca"],
    },
    "skhrc": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Human Rights Commission",
        },
        "url": {
            "en": "skhrc",
            "fr": "skhrc",
        },
        "court_id": ["sk hrc"],
    },
    "oic": {
        "jurisdiction": "ca",
        "name": {
            "en": "Information Commissioner of Canada",
            "fr": "Commissaire à l’information du Canada",
        },
        "url": {
            "en": "oic",
            "fr": "ci",
        },
        "court_id": ["oic", "ci"],
    },
    "nslb": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Labour Board",
        },
        "url": {
            "en": "nslb",
            "fr": "nslb",
        },
        "court_id": ["nslb", "ns lb", "nslrb"],
    },
    "qccm": {
        "jurisdiction": "qc",
        "name": {
            "en": "Municipal Courts",
            "fr": "Cours municipales",
        },
        "url": {
            "en": "qccm",
            "fr": "qccm",
        },
        "court_id": ["qccm", "qc cm"],
    },
    "nsla": {
        "jurisdiction": "ns",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "nsla",
            "fr": "nsla",
        },
        "court_id": ["nsla", "ns la"],
    },
    "skmt": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Master of Titles",
        },
        "url": {
            "en": "skmt",
            "fr": "skmt",
        },
        "court_id": ["sk mt"],
    },
    "onwsiat": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Workplace Safety and Insurance Appeals Tribunal",
        },
        "url": {
            "en": "onwsiat",
            "fr": "ontaspaat",
        },
        "court_id": ["onwsiat", "on wsiat", "ontaspaat"],
    },
    "skhrt": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Human Rights Tribunal",
        },
        "url": {
            "en": "skhrt",
            "fr": "skhrt",
        },
        "court_id": ["skhrt", "sk hrt"],
    },
    "bcpc": {
        "jurisdiction": "bc",
        "name": {
            "en": "Provincial Court of British Columbia",
        },
        "url": {
            "en": "bcpc",
            "fr": "bcpc",
        },
        "court_id": ["bcpc", "bc pc"],
    },
    "oncrb": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Custody Review Board",
            "fr": "Commission de révision des placements sous garde de l'Ontario",
        },
        "url": {
            "en": "oncrb",
            "fr": "oncrb",
        },
        "court_id": ["oncrb"],
    },
    "qccmeq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Corporation des maîtres électriciens du Québec",
        },
        "url": {
            "en": "qccmeq",
            "fr": "qccmeq",
        },
        "court_id": ["qccmeq"],
    },
    "citt-tcce": {
        "jurisdiction": "ca",
        "name": {
            "en": "Canadian International Trade Tribunal",
            "fr": "Tribunal canadien du commerce extérieur",
        },
        "url": {
            "en": "citt",
            "fr": "tcce",
        },
        "court_id": ["ca tcce", "ca citt"],
    },
    "abqb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Court of King's Bench of Alberta",
            "fr": "Cour du banc du Roi de l'Alberta",
        },
        "url": {
            "en": "abkb",
            "fr": "abkb",
        },
        "court_id": ["abqb", "abkb", "ab qb", "ab kb"],
    },
    "oncoto": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Occupational Therapists of Ontario",
            "fr": "Ordre des Ergothérapeutes de l'Ontario",
        },
        "url": {
            "en": "oncot",
            "fr": "oncot",
        },
        "court_id": ["oncot"],
    },
    "bcsec": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia Securities Commission",
        },
        "url": {
            "en": "bcsec",
            "fr": "bcsec",
        },
        "court_id": ["bcseccom"],
    },
    "qcopgq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Ordre professionnel des géologues du Québec",
        },
        "url": {
            "en": "qcopgq",
            "fr": "qcopgq",
        },
        "court_id": ["qc opgq"],
    },
    "ytla": {
        "jurisdiction": "yk",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "ytla",
            "fr": "ytla",
        },
        "court_id": ["yt la"],
    },
    "nbleb": {
        "jurisdiction": "nb",
        "name": {
            "en": "New Brunswick Labour and Employment Board",
            "fr": "Commission du travail et de l'emploi du Nouveau Brunswick",
        },
        "url": {
            "en": "nbleb",
            "fr": "nbcte",
        },
        "court_id": ["nb leb", "nb cte"],
    },
    "mbls": {
        "jurisdiction": "mb",
        "name": {
            "en": "Law Society of Manitoba",
            "fr": "Société du Barreau du Manitoba",
        },
        "url": {
            "en": "mbls",
            "fr": "mbsb",
        },
        "court_id": ["mbls", "mb ls", "mbsb"],
    },
    "nslrb": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Labour Relations Board",
        },
        "url": {
            "en": "nslrb",
            "fr": "nslrb",
        },
        "court_id": ["ns lrb"],
    },
    "mblb": {
        "jurisdiction": "mb",
        "name": {
            "en": "Manitoba Labour Board",
        },
        "url": {
            "en": "mblb",
            "fr": "mblb",
        },
        "court_id": ["mb lb"],
    },
    "skla": {
        "jurisdiction": "sk",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "skla",
            "fr": "skla",
        },
        "court_id": ["sk la"],
    },
    "abpc": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Court of Justice",
            "fr": "Cour de justice de l'Alberta",
        },
        "url": {
            "en": "abcj",
            "fr": "abcj",
        },
        "court_id": ["abpc", "ab pc", "abcj", "ab cj"],
    },
    "mbla": {
        "jurisdiction": "mb",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "mbla",
            "fr": "mbla",
        },
        "court_id": ["mb la"],
    },
    "ntls": {
        "jurisdiction": "nt",
        "name": {
            "en": "Law Society of the Northwest Territories",
        },
        "url": {
            "en": "ntls",
            "fr": "ntls",
        },
        "court_id": ["nwt ls"],
    },
    "abeab": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Environmental Appeal Board",
        },
        "url": {
            "en": "abeab",
            "fr": "abeab",
        },
        "court_id": ["abeab"],
    },
    "oncicb": {
        "jurisdiction": "on",
        "name": {
            "en": "Criminal Injuries Compensation Board",
            "fr": "Commission d’indemnisation des victimes d’actes criminels",
        },
        "url": {
            "en": "oncicb",
            "fr": "oncivac",
        },
        "court_id": ["oncicb", "oncivac"],
    },
    "nbbihra": {
        "jurisdiction": "nb",
        "name": {
            "en": "Board of Inquiry Under the Human Rights Act",
            "fr": "Commission d'enquête établie en vertu de la Loi sur les droits de la personne",
        },
        "url": {
            "en": "nbbihra",
            "fr": "nbbihra",
        },
        "court_id": ["nb bhr"],
    },
    "capsdpt": {
        "jurisdiction": "ca",
        "name": {
            "en": "Public Servants Disclosure Protection Tribunal",
            "fr": "Tribunal de la protection des fonctionnaires divulgateurs",
        },
        "url": {
            "en": "psdpt",
            "fr": "tpfd",
        },
        "court_id": ["tpfd", "psdpt"],
    },
    "nbls": {
        "jurisdiction": "nb",
        "name": {
            "en": "Law Society of New Brunswick",
            "fr": "Barreau du Nouveau-Brunswick",
        },
        "url": {
            "en": "nblsb",
            "fr": "nblsb",
        },
        "court_id": ["nblsb"],
    },
    "onafraat": {
        "jurisdiction": "on",
        "name": {
            "en": "Agriculture, Food & Rural Affairs Appeal Tribunal",
            "fr": "Tribunal d'appel de l'agriculture, de l'alimentation et des affaires rurales",
        },
        "url": {
            "en": "onafraat",
            "fr": "onafraat",
        },
        "court_id": ["onafraat"],
    },
    "ablerb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Law Enforcement Review Board",
        },
        "url": {
            "en": "ablerb",
            "fr": "ablerb",
        },
        "court_id": ["ablerb", "ab lerb"],
    },
    "nbla": {
        "jurisdiction": "nb",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "nbla",
            "fr": "nbla",
        },
        "court_id": ["nb la"],
    },
    "pela": {
        "jurisdiction": "pe",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "pela",
            "fr": "pela",
        },
        "court_id": ["pe la"],
    },
    "qcoapq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des audioprothésistes du Québec",
        },
        "url": {
            "en": "qcoapq",
            "fr": "qcoapq",
        },
        "court_id": ["qccdap", "qc oapq"],
    },
    "bcrb": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia Review Board",
        },
        "url": {
            "en": "bcrb",
            "fr": "bcrb",
        },
        "court_id": ["bcrb"],
    },
    "qccai": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission d'accès à l'information",
        },
        "url": {
            "en": "qccai",
            "fr": "qccai",
        },
        "court_id": ["qccai", "qc cai"],
    },
    "qctaa": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Tribunal d'arbitrage (performing, recording and film artists)",
        },
        "url": {
            "en": "qctaa",
            "fr": "qctaa",
        },
        "court_id": ["qcta", "qc taa"],
    },
    "qccdoooq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des opticiens d'ordonnances du Québec",
        },
        "url": {
            "en": "qccdoooq",
            "fr": "qccdoooq",
        },
        "court_id": ["qccdood", "qc cdoooq"],
    },
    "bclrb": {
        "jurisdiction": "bc",
        "name": {
            "en": "Labour Relations Board",
        },
        "url": {
            "en": "bclrb",
            "fr": "bclrb",
        },
        "court_id": ["bclrb", "bc lrb"],
    },
    "nssec": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Securities Commission",
        },
        "url": {
            "en": "nssec",
            "fr": "nssec",
        },
        "court_id": ["nssec", "ns sec"],
    },
    "onmlc": {
        "jurisdiction": "on",
        "name": {
            "en": "Mining and Lands Tribunal",
            "fr": "Tribunal des mines et des terres",
        },
        "url": {
            "en": "onmlt",
            "fr": "ontmt",
        },
        "court_id": ["on mlt", "on tmt"],
    },
    "skpmb": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Provincial Mediation Board",
        },
        "url": {
            "en": "skpmb",
            "fr": "skpmb",
        },
        "court_id": ["skpmb"],
    },
    "qcottiaq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des traducteurs, terminologues et interprètes agréés du Québec",
        },
        "url": {
            "en": "qcottiaq",
            "fr": "qcottiaq",
        },
        "court_id": ["qc ottiaq"],
    },
    "cer-rec": {
        "jurisdiction": "ca",
        "name": {
            "en": "Canada Energy Regulator",
            "fr": "Régie de l’énergie du Canada",
        },
        "url": {
            "en": "cer",
            "fr": "rec",
        },
        "court_id": ["ca cer", "ca rec"],
    },
    "nbomb": {
        "jurisdiction": "nb",
        "name": {
            "en": "Ombud New Brunswick",
            "fr": "Ombud Nouveau-Brunswick",
        },
        "url": {
            "en": "nbombud",
            "fr": "nbombud",
        },
        "court_id": ["nbombud", "nb ombud", "nbomb"],
    },
    "casa-cala": {
        "jurisdiction": "ca",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "cala",
            "fr": "casa",
        },
        "court_id": ["ca la", "ca sa"],
    },
    "qctat": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Tribunal administratif du travail",
        },
        "url": {
            "en": "qctat",
            "fr": "qctat",
        },
        "court_id": ["qctat", "qc tat"],
    },
    "qccq": {
        "jurisdiction": "qc",
        "name": {
            "en": "Court of Quebec",
            "fr": "Cour du Québec",
        },
        "url": {
            "en": "qccq",
            "fr": "qccq",
        },
        "court_id": ["qccq", "qc cq"],
    },
    "qctaq": {
        "jurisdiction": "qc",
        "name": {
            "en": "Administrative Tribunal of Québec",
            "fr": "Tribunal administratif du Québec",
        },
        "url": {
            "en": "qctaq",
            "fr": "qctaq",
        },
        "court_id": ["qc taq"],
    },
    "qccs": {
        "jurisdiction": "qc",
        "name": {
            "en": "Superior Court",
            "fr": "Cour supérieure",
        },
        "url": {
            "en": "qccs",
            "fr": "qccs",
        },
        "court_id": ["qccs", "qc cs"],
    },
    "oncocoo": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Chiropodists of Ontario",
        },
        "url": {
            "en": "oncocoo",
            "fr": "oncocoo",
        },
        "court_id": ["oncocoo", "on cocoo"],
    },
    "qcct": {
        "jurisdiction": "qc",
        "name": {
            "en": "Labour Commissioner",
            "fr": "Commissaire au travail",
        },
        "url": {
            "en": "qcct",
            "fr": "qcct",
        },
        "court_id": ["qc ct"],
    },
    "tmob": {
        "jurisdiction": "ca",
        "name": {
            "en": "Trademarks Opposition Board",
            "fr": "Commission des oppositions des marques de commerce",
        },
        "url": {
            "en": "tmob",
            "fr": "comc",
        },
        "court_id": ["tmob", "comc"],
    },
    "qcoaciq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Comité de discipline de l'organisme d'autoréglementation du courtage immobilier du Québec",
        },
        "url": {
            "en": "qcoaciq",
            "fr": "qcoaciq",
        },
        "court_id": ["qc oaciq"],
    },
    "onmic": {
        "jurisdiction": "on",
        "name": {
            "en": "Municipal Integrity Commissioners of Ontario",
            "fr": "Commissaires à l'intégrité municipaux de l'Ontario",
        },
        "url": {
            "en": "onmic",
            "fr": "onmic",
        },
        "court_id": ["onmic"],
    },
    "onca": {
        "jurisdiction": "on",
        "name": {
            "en": "Court of Appeal for Ontario",
            "fr": "Cour d'appel de l'Ontario",
        },
        "url": {
            "en": "onca",
            "fr": "onca",
        },
        "court_id": ["onca", "on ca"],
    },
    "nspc": {
        "jurisdiction": "ns",
        "name": {
            "en": "Provincial Court of Nova Scotia",
        },
        "url": {
            "en": "nspc",
            "fr": "nspc",
        },
        "court_id": ["nspc", "ns pc"],
    },
    "abreca": {
        "jurisdiction": "ab",
        "name": {
            "en": "Real Estate Council of Alberta",
        },
        "url": {
            "en": "abreca",
            "fr": "abreca",
        },
        "court_id": ["abreca", "ab reca"],
    },
    "oncvo": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Veterinarians of Ontario",
        },
        "url": {
            "en": "oncvo",
            "fr": "oncvo",
        },
        "court_id": ["oncvo"],
    },
    "mbqb": {
        "jurisdiction": "mb",
        "name": {
            "en": "Court of King's Bench of Manitoba",
            "fr": "Cour du Banc du Roi du Manitoba",
        },
        "url": {
            "en": "mbkb",
            "fr": "mbkb",
        },
        "court_id": ["mbqb", "mb qb", "mbkb", "mb kb"],
    },
    "sct-trp": {
        "jurisdiction": "ca",
        "name": {
            "en": "Specific Claims Tribunal Canada",
            "en": "Tribunal des revendications particulières Canada",
        },
        "url": {
            "en": "sct",
            "fr": "trp",
        },
        "court_id": ["sctc", "trpc"],
    },
    "skqb": {
        "jurisdiction": "sk",
        "name": {
            "en": "Court of King's Bench for Saskatchewan",
        },
        "url": {
            "en": "skkb",
            "fr": "skkb",
        },
        "court_id": ["skqb", "sk qb", "skkb", "sk kb"],
    },
    "onarb": {
        "jurisdiction": "on",
        "name": {
            "en": "Assessment Review Board",
            "fr": "Commission de révision de l'évaluation foncière de l'Ontario",
        },
        "url": {
            "en": "onarb",
            "fr": "oncref",
        },
        "court_id": ["on arb", "on cref"],
    },
    "ablrb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Labour Relations Board",
        },
        "url": {
            "en": "ablrb",
            "fr": "ablrb",
        },
        "court_id": ["alrb", "ab lrb"],
    },
    "qcdag": {
        "jurisdiction": "qc",
        "name": {
            "en": "Labour Arbitration Awards (including Conférence des arbitres)",
            "fr": "Sentences arbitrales de travail (incluant Conférence des arbitres)",
        },
        "url": {
            "en": "qcla",
            "fr": "qcsat",
        },
        "court_id": ["qc sat", "qc la"],
    },
    "peirac": {
        "jurisdiction": "pe",
        "name": {
            "en": "Prince Edward Island Regulatory & Appeals Commission",
            "fr": "Commission de réglementation et d'appels de l'Île-du-Prince-Édouard",
        },
        "url": {
            "en": "peirac",
            "fr": "peirac",
        },
        "court_id": ["peirac", "pe irac"],
    },
    "sklgb": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Local Government Board",
        },
        "url": {
            "en": "sklgb",
            "fr": "sklgb",
        },
        "court_id": ["sk lgb"],
    },
    "onctcmpao": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Traditional Chinese Medicine Practitioners and Acupuncturists of Ontario",
            "fr": "Ordre des praticiens en médecine traditionnelle chinoise et des acupuncteurs de l'Ontario",
        },
        "url": {
            "en": "onctcmpao",
            "fr": "onctcmpao",
        },
        "court_id": ["onctcmpao"],
    },
    "bcsp": {
        "jurisdiction": "bc",
        "name": {
            "en": "Superintendent of Pensions",
        },
        "url": {
            "en": "bcsp",
            "fr": "bcsp",
        },
        "court_id": ["bcsp"],
    },
    "ntlsb": {
        "jurisdiction": "nt",
        "name": {
            "en": "Employment Standards Appeals Office",
        },
        "url": {
            "en": "ntlsb",
            "fr": "ntlsb",
        },
        "court_id": ["nwt lsb"],
    },
    "mbpc": {
        "jurisdiction": "mb",
        "name": {
            "en": "Provincial Court of Manitoba",
            "fr": "Cour provinciale du Manitoba",
        },
        "url": {
            "en": "mbpc",
            "fr": "mbpc",
        },
        "court_id": ["mbpc", "mb pc"],
    },
    "skpc": {
        "jurisdiction": "sk",
        "name": {
            "en": "Provincial Court of Saskatchewan",
            "fr": "Cour provinciale de la Saskatchewan",
        },
        "url": {
            "en": "skpc",
            "fr": "skpc",
        },
        "court_id": ["skpc", "sk pc"],
    },
    "bcsc": {
        "jurisdiction": "bc",
        "name": {
            "en": "Supreme Court of British Columbia",
        },
        "url": {
            "en": "bcsc",
            "fr": "bcsc",
        },
        "court_id": ["bcsc", "bc sc"],
    },
    "abgaa": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Grievance Arbitration Awards",
        },
        "url": {
            "en": "abgaa",
            "fr": "abgaa",
        },
        "court_id": ["ab gaa"],
    },
    "onscdc": {
        "jurisdiction": "on",
        "name": {
            "en": "Divisional Court",
            "fr": "Cour divisionnaire",
        },
        "url": {
            "en": "onscdc",
            "fr": "onscdc",
        },
        "court_id": ["onsc", "on scdc", "oncs", "on cs"],
    },
    "nttc": {
        "jurisdiction": "nt",
        "name": {
            "en": "Territorial Court of the Northwest Territories",
        },
        "url": {
            "en": "nttc",
            "fr": "nttc",
        },
        "court_id": ["nwttc", "nwt tc"],
    },
    "qcrbq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Régie du Bâtiment - licences d'entrepreneur de construction",
        },
        "url": {
            "en": "qcrbq",
            "fr": "qcrbq",
        },
        "court_id": ["qcrbq", "qc rbq"],
    },
    "nbwhscc": {
        "jurisdiction": "nb",
        "name": {
            "en": "Workers’ Compensation Appeals Tribunal",
            "fr": "Tribunal d'appel des accidents au travail",
        },
        "url": {
            "en": "nbwcat",
            "fr": "nbtaat",
        },
        "court_id": ["nb wcat", "nb taat"],
    },
    "ntaat": {
        "jurisdiction": "nt",
        "name": {
            "en": "Northwest Territories Assessment Appeal Tribunal",
        },
        "url": {
            "en": "ntaat",
            "fr": "ntaat",
        },
        "court_id": ["nwtaat"],
    },
    "onrcdso": {
        "jurisdiction": "on",
        "name": {
            "en": "Royal College of Dental Surgeons of Ontario",
            "fr": "Collège royal des chirurgiens dentistes de l'Ontario",
        },
        "url": {
            "en": "onrcdso",
            "fr": "onrcdso",
        },
        "court_id": ["onrcdso", "on rcdso"],
    },
    "sksu": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Surrogate Court",
        },
        "url": {
            "en": "sksu",
            "fr": "sksu",
        },
        "court_id": ["sk su"],
    },
    "bcitab": {
        "jurisdiction": "bc",
        "name": {
            "en": "Skilled Trades BC Appeal Board",
        },
        "url": {
            "en": "bcstab",
            "fr": "bcstab",
        },
        "court_id": ["bcitab"],
    },
    "nbpc": {
        "jurisdiction": "nb",
        "name": {
            "en": "Provincial Court",
            "fr": "Cour provinciale",
        },
        "url": {
            "en": "nbpc",
            "fr": "nbpc",
        },
        "court_id": ["nbpc", "nb pc"],
    },
    "qcces": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission de l'équité salariale",
        },
        "url": {
            "en": "qcces",
            "fr": "qcces",
        },
        "court_id": ["qc ces"],
    },
    "ondr": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Court of the Drainage Referee",
            "fr": "Arbitre en matière de drainage de l'Ontario",
        },
        "url": {
            "en": "ondr",
            "fr": "ondr",
        },
        "court_id": ["ondr"],
    },
    "bcorl": {
        "jurisdiction": "bc",
        "name": {
            "en": "Office of the Registrar of Lobbyists",
        },
        "url": {
            "en": "bcorl",
            "fr": "bcorl",
        },
        "court_id": ["bcorl"],
    },
    "ykhrc": {
        "jurisdiction": "yk",
        "name": {
            "en": "Yukon Human Rights Commission (Board of Adjudication)",
            "fr": "Commission des droits de la personne du Yukon (conseil d'arbitrage)",
        },
        "url": {
            "en": "ykhrc",
            "fr": "ykhrc",
        },
        "court_id": ["yk hrc"],
    },
    "pepc": {
        "jurisdiction": "pe",
        "name": {
            "en": "Provincial Court of Prince Edward Island",
        },
        "url": {
            "en": "pepc",
            "fr": "pepc",
        },
        "court_id": ["pe pc"],
    },
    "bcccalab": {
        "jurisdiction": "bc",
        "name": {
            "en": "Community Care and Assisted Living Appeal Board",
        },
        "url": {
            "en": "bcccalab",
            "fr": "bcccalab",
        },
        "court_id": ["bcccalab"],
    },
    "nlsctd": {
        "jurisdiction": "nl",
        "name": {
            "en": "Supreme Court of Newfoundland and Labrador",
        },
        "url": {
            "en": "nlsc",
            "fr": "nlsc",
        },
        "court_id": ["nlsc", "nl sc", "nlsctd", "nltd"],
    },
    "skmbr": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Municipal Boards of Revision",
        },
        "url": {
            "en": "skmbr",
            "fr": "skmbr",
        },
        "court_id": ["skmbr"],
    },
    "ntsc": {
        "jurisdiction": "nt",
        "name": {
            "en": "Supreme Court of the Northwest Territories",
            "fr": "Cour suprême des Territoires du Nord-Ouest",
        },
        "url": {
            "en": "ntsc",
            "fr": "ntsc",
        },
        "court_id": ["nwtsc", "ntsc", "nwt sc"],
    },
    "oncrpo": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Registered Psychotherapists and Registered Mental Health Therapists of Ontario",
        },
        "url": {
            "en": "oncrpo",
            "fr": "oncrpo",
        },
        "court_id": ["oncrpo"],
    },
    "nlca": {
        "jurisdiction": "nl",
        "name": {
            "en": "Court of Appeal of Newfoundland and Labrador",
        },
        "url": {
            "en": "nlca",
            "fr": "nlca",
        },
        "court_id": ["nlca", "nl ca"],
    },
    "ntro": {
        "jurisdiction": "nt",
        "name": {
            "en": "Rental Officer",
            "fr": "Régisseur des loyers",
        },
        "url": {
            "en": "ntro",
            "fr": "ntro",
        },
        "court_id": ["nwt ro"],
    },
    "nuipc": {
        "jurisdiction": "nu",
        "name": {
            "en": "Information and Privacy Commissioner",
        },
        "url": {
            "en": "nuipc",
            "fr": "nuipc",
        },
        "court_id": ["nuipc"],
    },
    "onhrap": {
        "jurisdiction": "on",
        "name": {
            "en": "Horse Racing Appeal Panel",
            "fr": "Comité d’appel des courses de chevaux",
        },
        "url": {
            "en": "onhrap",
            "fr": "oncacc",
        },
        "court_id": ["on hrap", "on cacc"],
    },
    "oncj": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Court of Justice",
            "fr": "Cour de justice de l'Ontario",
        },
        "url": {
            "en": "oncj",
            "fr": "oncj",
        },
        "court_id": ["oncj", "on cj"],
    },
    "cart-crac": {
        "jurisdiction": "ca",
        "name": {
            "en": "Canada Agricultural Review Tribunal",
            "fr": "Commission de révision agricole du Canada",
        },
        "url": {
            "en": "cart",
            "fr": "crac",
        },
        "court_id": ["cart", "ca art", "crac", "ca cra"],
    },
    "bcfac": {
        "jurisdiction": "bc",
        "name": {
            "en": "Forest Appeals Commission",
        },
        "url": {
            "en": "bcfac",
            "fr": "bcfac",
        },
        "court_id": ["bcfac"],
    },
    "nspr": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Probate Court",
        },
        "url": {
            "en": "nspr",
            "fr": "nspr",
        },
        "court_id": [
            "nspb",
            "ns pr",
        ],
    },
    "qccdp": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Tribunal administratif de déontologie policière",
        },
        "url": {
            "en": "qctadp",
            "fr": "qctadp",
        },
        "court_id": ["qctadp", "qc tadp", "chrc cdp", "qc tdap", "qc cdp", "qccdp"],
    },
    "onco": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Optometrists of Ontario",
        },
        "url": {
            "en": "onco",
            "fr": "onco",
        },
        "court_id": ["onco"],
    },
    "ykca": {
        "jurisdiction": "yk",
        "name": {
            "en": "Court of Appeal of Yukon",
            "fr": "Cour d'appel du Yukon",
        },
        "url": {
            "en": "ykca",
            "fr": "ykca",
        },
        "court_id": ["ykca", "yk ca"],
    },
    "qctdp": {
        "jurisdiction": "qc",
        "name": {
            "en": "Human Rights Tribunal",
            "fr": "Tribunal des droits de la personne",
        },
        "url": {
            "en": "qctdp",
            "fr": "qctdp",
        },
        "court_id": ["qctdp", "qc tdp", "cq tdp", "tdp qc", "tdp cq"],
    },
    "qccmnq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission municipale du Québec",
        },
        "url": {
            "en": "qccmnq",
            "fr": "qccmnq",
        },
        "court_id": ["qc cmnq"],
    },
    "qcoppq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel de la physiothérapie du Québec",
        },
        "url": {
            "en": "qcoppq",
            "fr": "qcoppq",
        },
        "court_id": ["qccdoppq", "qc oppq"],
    },
    "qccdoii": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des infirmières et infirmiers du Québec",
        },
        "url": {
            "en": "qccdoii",
            "fr": "qccdoii",
        },
        "court_id": ["qccdinf", "qc cdoii"],
    },
    "ntipc": {
        "jurisdiction": "nt",
        "name": {
            "en": "Northwest Territories Information and Privacy Commissioner",
        },
        "url": {
            "en": "ntipc",
            "fr": "ntipc",
        },
        "court_id": ["ntipc", "nwt ipc"],
    },
    "qcoarq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des architectes du Québec",
        },
        "url": {
            "en": "qcoarq",
            "fr": "qcoarq",
        },
        "court_id": ["qc oarq", "qccdarc"],
    },
    "mbcpsdc": {
        "jurisdiction": "mb",
        "name": {
            "en": "College of Physicians & Surgeons of Manitoba Discipline Committee",
            "fr": "Comité de discipline du Collège des médecins et des chirurgiens du Manitoba",
        },
        "url": {
            "en": "mbcpsdc",
            "fr": "mbcpsdc",
        },
        "court_id": ["mbcpsdc"],
    },
    "forep": {
        "jurisdiction": "ca",
        "name": {
            "en": "Foreign reported decisions",
            "fr": "Décisions rapportées à l'étranger",
        },
        "url": {
            "en": "forep",
            "fr": "etrap",
        },
        "court_id": ["forep"],
    },
    "nssc": {
        "jurisdiction": "ns",
        "name": {
            "en": "Supreme Court of Nova Scotia",
        },
        "url": {
            "en": "nssc",
            "fr": "nssc",
        },
        "court_id": ["nssc", "ns sc"],
    },
    "nssf": {
        "jurisdiction": "ns",
        "name": {
            "en": "Supreme Court of Nova Scotia (Family Division)",
        },
        "url": {
            "en": "nssf",
            "fr": "nssf",
        },
        "court_id": ["nssf", "ns sf"],
    },
    "nssm": {
        "jurisdiction": "ns",
        "name": {
            "en": "Small Claims Court",
        },
        "url": {
            "en": "nssm",
            "fr": "nssm",
        },
        "court_id": ["nssm"],
    },
    "onnfppb": {
        "jurisdiction": "on",
        "name": {
            "en": "Normal Farm Practices Protection Board",
            "fr": "Commission de protection des pratiques agricoles normales",
        },
        "url": {
            "en": "onnfppb",
            "fr": "onnfppb",
        },
        "court_id": ["onnfppb"],
    },
    "absdab": {
        "jurisdiction": "ab",
        "name": {
            "en": "Calgary Subdivision & Development Appeal Board",
        },
        "url": {
            "en": "absdab",
            "fr": "absdab",
        },
        "court_id": ["ab sdab", "cgysdab"],
    },
    "bceab": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia Environmental Appeal Board",
        },
        "url": {
            "en": "bceab",
            "fr": "bceab",
        },
        "court_id": ["bceab"],
    },
    "nbqb": {
        "jurisdiction": "nb",
        "name": {
            "en": "Court of King's Bench of New Brunswick",
            "fr": "Cour du Banc du Roi du Nouveau-Brunswick",
        },
        "url": {
            "en": "nbkb",
            "fr": "nbbr",
        },
        "court_id": ["nbqb", "nbkb", "nb qb", "nb kb", "nbbr", "nb br"],
    },
    "nshrc": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Human Rights Commission",
        },
        "url": {
            "en": "nshrc",
            "fr": "nshrc",
        },
        "court_id": ["ns hrc"],
    },
    "qccdoiia": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des infirmières et infirmiers auxiliaires du Québec",
        },
        "url": {
            "en": "qccdoiia",
            "fr": "qccdoiia",
        },
        "court_id": ["qc oiia", "qccdia"],
    },
    "mbhab": {
        "jurisdiction": "mb",
        "name": {
            "en": "Manitoba Health Appeal Board",
            "fr": "Conseil manitobain d’appel en matière de santé",
        },
        "url": {
            "en": "mbhab",
            "fr": "mbhab",
        },
        "court_id": ["mb hab"],
    },
    "qccraaap": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission de reconnaissance des associations d'artistes et des associations de producteurs",
        },
        "url": {
            "en": "qccraaap",
            "fr": "qccraaap",
        },
        "court_id": ["qc craaap", "craaap"],
    },
    "onlrb": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Labour Relations Board",
            "fr": "Commission des relations de travail de l'Ontario",
        },
        "url": {
            "en": "onlrb",
            "fr": "onlrb",
        },
        "court_id": ["on lrb"],
    },
    "qccdcsf": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Comité de discipline de la Chambre de la sécurité financière",
        },
        "url": {
            "en": "qccdcsf",
            "fr": "qccdcsf",
        },
        "court_id": ["qccdcsf", "qc cdcsf"],
    },
    "abohsab": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Occupational Health and Safety Appeal decisions",
        },
        "url": {
            "en": "abohsab",
            "fr": "abohsab",
        },
        "court_id": ["abohsab"],
    },
    "skort": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Office of Residential Tenancies",
        },
        "url": {
            "en": "skort",
            "fr": "skort",
        },
        "court_id": ["skort"],
    },
    "nuyc": {
        "jurisdiction": "nu",
        "name": {
            "en": "Youth Justice Court of Nunavut",
            "fr": "Tribunal de la jeunesse du Nunavut",
        },
        "url": {
            "en": "nuyc",
            "fr": "nuyc",
        },
        "court_id": ["yjcn"],
    },
    "oncaspd": {
        "jurisdiction": "on",
        "name": {
            "en": "College of Audiologists and Speech-Language Pathologists of Ontario",
            "fr": "Ordre des audiologistes et des orthophonistes de l’Ontario",
        },
        "url": {
            "en": "oncaspd",
            "fr": "oncaspd",
        },
        "court_id": ["oncaspd"],
    },
    "bcwcat": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia Workers' Compensation Appeal Tribunal",
        },
        "url": {
            "en": "bcwcat",
            "fr": "bcwcat",
        },
        "court_id": ["bc wcat"],
    },
    "bcogat": {
        "jurisdiction": "bc",
        "name": {
            "en": "Energy Resource Appeal Tribunal",
        },
        "url": {
            "en": "bcerat",
            "fr": "bcerat",
        },
        "court_id": ["bcogat"],
    },
    "qccdoiq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des ingénieurs du Québec",
        },
        "url": {
            "en": "qccdoiq",
            "fr": "qccdoiq",
        },
        "court_id": ["qc cdoiq", "qccding"],
    },
    "nthrap": {
        "jurisdiction": "nt",
        "name": {
            "en": "Human Rights Adjudication Panel",
            "fr": "Tribunal d'arbitrage des droits de la personne",
        },
        "url": {
            "en": "nthrap",
            "fr": "nttadp",
        },
        "court_id": ["nt tadp", "nt hrap"],
    },
    "bchab": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia Hospital Appeal Board",
        },
        "url": {
            "en": "bchab",
            "fr": "bchab",
        },
        "court_id": ["bchab"],
    },
    "ukpc": {
        "jurisdiction": "ca",
        "name": {
            "en": "Judicial Committee of the Privy Council - Canadian cases",
            "fr": "Comité judiciaire du Conseil privé - affaires canadiennes",
        },
        "url": {
            "en": "ukjcpc",
            "fr": "rucjcp",
        },
        "court_id": ["uk jcpc"],
    },
    "nsuarb": {
        "jurisdiction": "ns",
        "name": {
            "en": "Nova Scotia Utility and Review Board",
        },
        "url": {
            "en": "nsuarb",
            "fr": "nsuarb",
        },
        "court_id": ["nsuarb"],
    },
    "qcohdq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Ordre des hygiénistes dentaires du Québec",
        },
        "url": {
            "en": "qcohdq",
            "fr": "qcohdq",
        },
        "court_id": ["qccdhd", "qc ohdq"],
    },
    "fca": {
        "jurisdiction": "ca",
        "name": {
            "en": "Federal Court of Appeal",
            "fr": "Cour d'appel fédérale",
        },
        "url": {
            "en": "fca",
            "fr": "caf",
        },
        "court_id": ["fca", "caf"],
    },
    "qcrde": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Régie de l'énergie",
        },
        "url": {
            "en": "qcrde",
            "fr": "qcrde",
        },
        "court_id": ["qc rde"],
    },
    "camfda": {
        "jurisdiction": "ca",
        "name": {
            "en": "Mutual Fund Dealers Association of Canada",
            "fr": "Association canadienne des courtiers de fonds mutuels",
        },
        "url": {
            "en": "camfda",
            "fr": "caaccfm",
        },
        "court_id": ["camfda", "ca accfm", "ca mfdac"],
    },
    "qcoifq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des ingénieurs forestiers du Québec",
        },
        "url": {
            "en": "qcoifq",
            "fr": "qcoifq",
        },
        "court_id": ["qc oifq", "qccdingf"],
    },
    "qcrdl": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Tribunal administratif du logement",
        },
        "url": {
            "en": "qctal",
            "fr": "qctal",
        },
        "court_id": ["qc tal", "qctal"],
    },
    "fct": {
        "jurisdiction": "ca",
        "name": {
            "en": "Federal Court",
            "fr": "Cour fédérale",
        },
        "url": {
            "en": "fct",
            "fr": "cfpi",
        },
        "court_id": ["fc", "cf", "fct"],
    },
    "nllrb": {
        "jurisdiction": "nl",
        "name": {
            "en": "Newfoundland and Labrador Labour Relations Board",
        },
        "url": {
            "en": "nllrb",
            "fr": "nllrb",
        },
        "court_id": ["nllrb", "nl lrb"],
    },
    "pssrb": {
        "jurisdiction": "ca",
        "name": {
            "en": "Public Service Labour Relations Board",
            "fr": "Commission des relations de travail dans la fonction publique",
        },
        "url": {
            "en": "pssrb",
            "fr": "crtfp",
        },
        "court_id": ["pssrb", "crtfp", "pslrb"],
    },
    "skfca": {
        "jurisdiction": "sk",
        "name": {
            "en": "Saskatchewan Board of Review under the Farmers' Creditors Arrangement Act, 1934",
        },
        "url": {
            "en": "skfca",
            "fr": "skfca",
        },
        "court_id": ["sk fca"],
    },
    "qcopsq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des sexologues du Québec",
        },
        "url": {
            "en": "opsq",
            "fr": "opsq",
        },
        "court_id": ["qccdsexo", "qc opsq"],
    },
    "nusec": {
        "jurisdiction": "nu",
        "name": {
            "en": "Nunavut Registrar of Securities",
            "fr": "Bureau d'enregistrement du Nunavut",
        },
        "url": {
            "en": "nusec",
            "fr": "nusec",
        },
        "court_id": ["nu sec"],
    },
    "qccfp": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission de la fonction publique",
        },
        "url": {"en": "qccfp"},
        "court_id": ["qccfp", "qc cfp", "qc mff", "qc psc"],
    },
    "nlla": {
        "jurisdiction": "nl",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "nlla",
            "fr": "nlla",
        },
        "court_id": ["nl la"],
    },
    "onmb": {
        "jurisdiction": "on",
        "name": {
            "en": "Local Planning Appeal Tribunal",
            "fr": "Tribunal d’appel de l’aménagement local",
        },
        "url": {
            "en": "onlpat",
            "fr": "ontaal",
        },
        "court_id": ["on lpat", "on taal"],
    },
    "caiiroc": {
        "jurisdiction": "ca",
        "name": {
            "en": "Investment Industry Regulatory Organization of Canada",
            "fr": "Organisme canadien de réglementation du commerce des valeurs mobilières",
        },
        "url": {
            "en": "caiiroc",
            "fr": "ocrcvm",
        },
        "court_id": ["iroc", "ocrcvm", "ca ocrcvm", "ca iiroc", "iiroc"],
    },
    "nscps": {
        "jurisdiction": "ns",
        "name": {
            "en": "College of Physicians and Surgeons of Nova Scotia",
        },
        "url": {
            "en": "nscps",
            "fr": "nscps",
        },
        "court_id": ["ns cps"],
    },
    "abtsb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Transportation Safety Board",
        },
        "url": {
            "en": "abtsb",
            "fr": "abtsb",
        },
        "court_id": ["abtsb"],
    },
    "onsbt": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Social Benefits Tribunal",
            "fr": "Tribunal de l'aide sociale de l'Ontario",
        },
        "url": {
            "en": "onsbt",
            "fr": "onsbt",
        },
        "court_id": ["onsbt"],
    },
    "exchc-cech": {
        "jurisdiction": "ca",
        "name": {
            "en": "Exchequer Court of Canada",
            "fr": "Cour de l'Échiquier du Canada",
        },
        "url": {
            "en": "exch",
            "fr": "ech",
        },
        "court_id": ["ca céc", "ca exc"],
    },
    "onccb": {
        "jurisdiction": "on",
        "name": {
            "en": "Consent and Capacity Board",
            "fr": "Commission du consentement et de la capacité",
        },
        "url": {
            "en": "onccb",
            "fr": "onccb",
        },
        "court_id": ["on ccb"],
    },
    "iccrc": {
        "jurisdiction": "ca",
        "name": {
            "en": "College of Immigration and Citizenship Consultants",
            "fr": "Collège des consultants en immigration et en citoyenneté",
        },
        "url": {
            "en": "cicc",
            "fr": "ccic",
        },
        "court_id": ["ccic", "cicc", "iccrc", "crcic"],
    },
    "onpeht": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Pay Equity Hearings Tribunal",
            "fr": "Tribunal de l'équité salariale de l'Ontario",
        },
        "url": {
            "en": "onpeht",
            "fr": "onpeht",
        },
        "court_id": ["on peht"],
    },
    "qcodq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des dentistes du Québec",
        },
        "url": {
            "en": "qcodq",
            "fr": "qcodq",
        },
        "court_id": ["qccdodq", "qc odq"],
    },
    "ablcb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Land Compensation Board",
        },
        "url": {
            "en": "ablcb",
            "fr": "ablcb",
        },
        "court_id": ["ablcb", "ab lcb"],
    },
    "psst": {
        "jurisdiction": "ca",
        "name": {
            "en": "Public Service Staffing Tribunal",
            "fr": "Tribunal de la dotation de la fonction publique",
        },
        "url": {
            "en": "psst",
            "fr": "psst",
        },
        "court_id": ["psst", "tdfp"],
    },
    "onipc": {
        "jurisdiction": "on",
        "name": {
            "en": "Information and Privacy Commissioner Ontario",
            "fr": "Commissaire à l'information et à la protection de la vie privée de l'Ontario",
        },
        "url": {
            "en": "onipc",
            "fr": "onipc",
        },
        "court_id": ["on ipc"],
    },
    "onlt": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Land Tribunal",
            "fr": "Tribunal ontarien de l’aménagement du territoire",
        },
        "url": {
            "en": "onlt",
            "fr": "onlt",
        },
        "court_id": ["on lt"],
    },
    "qccmq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de la magistrature",
        },
        "url": {
            "en": "qccmq",
            "fr": "qccmq",
        },
        "court_id": ["qc cm"],
    },
    "onacrb": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Animal Care Review Board",
            "fr": "Commission d’étude des soins aux animaux de l'Ontario",
        },
        "url": {
            "en": "onacrb",
            "fr": "oncesa",
        },
        "court_id": ["onacrb", "on acrb", "on cesa", "oncesa"],
    },
    "bcsre": {
        "jurisdiction": "bc",
        "name": {
            "en": "Superintendent of Real Estate",
        },
        "url": {
            "en": "bcsre",
            "fr": "bcsre",
        },
        "court_id": ["bcsre"],
    },
    "bccrt": {
        "jurisdiction": "bc",
        "name": {
            "en": "Civil Resolution Tribunal of British Columbia",
        },
        "url": {
            "en": "bccrt",
            "fr": "bccrt",
        },
        "court_id": ["bccrt"],
    },
    "qcadmaq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des administrateurs agréés du Québec",
        },
        "url": {
            "en": "qcadmaq",
            "fr": "qcadmaq",
        },
        "court_id": ["qcadmaq", "qccdadma", "qc admaq"],
    },
    "onhsarb": {
        "jurisdiction": "on",
        "name": {
            "en": "Health Services Appeal and Review Board",
            "fr": "Commission d’appel et de révision des services de santé",
        },
        "url": {
            "en": "onhsarb",
            "fr": "oncarss",
        },
        "court_id": ["on hsarb", "oncarss"],
    },
    "onla": {
        "jurisdiction": "on",
        "name": {
            "en": "Labour Arbitration Awards",
            "fr": "Sentences arbitrales de travail",
        },
        "url": {
            "en": "onla",
            "fr": "onla",
        },
        "court_id": ["on la"],
    },
    "bcctc": {
        "jurisdiction": "bc",
        "name": {
            "en": "British Columbia Container Trucking Commissioner",
        },
        "url": {
            "en": "bcctc",
            "fr": "bcctc",
        },
        "court_id": ["bcctc"],
    },
    "absra": {
        "jurisdiction": "ab",
        "name": {
            "en": "SafeRoads Alberta",
        },
        "url": {
            "en": "absra",
            "fr": "absra",
        },
        "court_id": ["absra"],
    },
    "pcc-cvpc": {
        "jurisdiction": "ca",
        "name": {
            "en": "Privacy Commissioner of Canada",
            "fr": "Commissaire à la protection de la vie privée du Canada",
        },
        "url": {
            "en": "pcc",
            "fr": "cvpc",
        },
        "court_id": ["pcc", "cvpc"],
    },
    "absrb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Surface Rights Board",
        },
        "url": {
            "en": "absrb",
            "fr": "absrb",
        },
        "court_id": ["absrb"],
    },
    "qcocq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des chiropraticiens du Québec",
        },
        "url": {
            "en": "qcocq",
            "fr": "qcocq",
        },
        "court_id": ["qc ocq", "qccdchir"],
    },
    "qccdppq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline des psychoéducateurs et psychoéducatrices du Québec",
        },
        "url": {
            "en": "qccdppq",
            "fr": "qccdppq",
        },
        "court_id": ["qc cdppq", "qccdpsed"],
    },
    "ytrto": {
        "jurisdiction": "yk",
        "name": {
            "en": "Yukon Residential Tenancies Office",
        },
        "url": {
            "en": "ytrto",
            "fr": "ytrto",
        },
        "court_id": ["ytrto"],
    },
    "oncpdc": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario College of Pharmacists Discipline Committee",
            "fr": "Comité de discipline de l'Ordre des pharmaciens de l’Ontario",
        },
        "url": {
            "en": "oncpdc",
            "fr": "oncpdc",
        },
        "court_id": ["oncpdc"],
    },
    "qcclp": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission des lésions professionnelles du Québec",
        },
        "url": {
            "en": "qcclp",
            "fr": "qcclp",
        },
        "court_id": ["qcclp", "qc clp"],
    },
    "abcgyarb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Calgary Assessment Review Board",
        },
        "url": {
            "en": "abcgyarb",
            "fr": "abcgyarb",
        },
        "court_id": ["abcgyarb", "ab cgyarb"],
    },
    "qccdomv": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des médecins vétérinaires du Québec",
        },
        "url": {
            "en": "qccdomv",
            "fr": "qccdomv",
        },
        "court_id": ["qccdmv", "qc cdomv"],
    },
    "onlst": {
        "jurisdiction": "on",
        "name": {
            "en": "Law Society Tribunal",
            "fr": "Tribunal du Barreau",
        },
        "url": {
            "en": "onlst",
            "fr": "ontb",
        },
        "court_id": ["onlsth", "ontbh", "on lst", "onlsta", "onlsap", "onlst", "onlshp"],
    },
    "abmgb": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Municipal Government Board",
        },
        "url": {
            "en": "abmgb",
            "fr": "abmgb",
        },
        "court_id": ["abmgb"],
    },
    "cci-tcc": {
        "jurisdiction": "ca",
        "name": {
            "en": "Tax Court of Canada",
            "fr": "Cour canadienne de l'impôt",
        },
        "url": {
            "en": "tcc",
            "fr": "cci",
        },
        "court_id": ["cci", "tcc"],
    },
    "nuhrt": {
        "jurisdiction": "nu",
        "name": {
            "en": "Nunavut Human Rights Tribunal",
            "fr": "Tribunal des droits de la personne du Nunavut",
        },
        "url": {
            "en": "nuhrt",
            "fr": "nuhrt",
        },
        "court_id": ["nhrt"],
    },
    "qcotstcfq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des travailleurs sociaux et des thérapeutes conjugaux et familiaux du Québec",
        },
        "url": {
            "en": "qcotstcfq",
            "fr": "qcotstcfq",
        },
        "court_id": ["qc otstcfq", "qccdtstcf"],
    },
    "onpsgb": {
        "jurisdiction": "on",
        "name": {
            "en": "Ontario Public Service Grievance Board",
            "fr": "Commission des griefs de la fonction publique de l'Ontario",
        },
        "url": {
            "en": "onpsgb",
            "fr": "oncgfp",
        },
        "court_id": ["on psgb", "on cgfp"],
    },
    "onltb": {
        "jurisdiction": "on",
        "name": {
            "en": "Landlord and Tenant Board",
            "fr": "Commission de la location immobilière",
        },
        "url": {
            "en": "onltb",
            "fr": "oncll",
        },
        "court_id": ["onltb", "on ltb"],
    },
    "oncat": {
        "jurisdiction": "on",
        "name": {
            "en": "Condominium Authority Tribunal",
            "fr": "Tribunal de l'autorité du secteur des condominiums",
        },
        "url": {
            "en": "oncat",
            "fr": "ontasc",
        },
        "court_id": ["oncat", "ontasc"],
    },
    "peihrc": {
        "jurisdiction": "pe",
        "name": {
            "en": "Prince Edward Island Human Rights Commission",
            "fr": "Commission des droits de la personne de l'Île-du-Prince-Édouard",
        },
        "url": {
            "en": "peihrc",
            "fr": "peicdp",
        },
        "court_id": ["pe hrc"],
    },
    "pelrb": {
        "jurisdiction": "pe",
        "name": {
            "en": "Prince Edward Island Labour Relations Board",
        },
        "url": {
            "en": "pelrb",
            "fr": "pelrb",
        },
        "court_id": ["pe lrb"],
    },
    "nlipc": {
        "jurisdiction": "nl",
        "name": {
            "en": "Information and Privacy Commissioner",
        },
        "url": {
            "en": "nlipc",
            "fr": "nlipc",
        },
        "court_id": ["nl ipc"],
    },
    "qcagq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des agronomes du Québec",
        },
        "url": {
            "en": "qcagq",
            "fr": "qcagq",
        },
        "court_id": ["qc agq", "qccdagr"],
    },
    "qcoeaq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des évaluateurs agréés du Québec",
        },
        "url": {
            "en": "qcoeaq",
            "fr": "qcoeaq",
        },
        "court_id": ["qc oeaq", "qccdea"],
    },
    "ablcsab": {
        "jurisdiction": "ab",
        "name": {
            "en": "Alberta Licence and Community Standards Appeal Board",
        },
        "url": {
            "en": "ablcsab",
            "fr": "ablcsab",
        },
        "court_id": ["ablcsab"],
    },
    "ohstc": {
        "jurisdiction": "ca",
        "name": {
            "en": "Occupational Health and Safety Tribunal Canada",
            "fr": "Tribunal de santé et sécurité au travail Canada",
        },
        "url": {
            "en": "ohstc",
            "fr": "tsstc",
        },
        "court_id": ["ohstc", "tsstc"],
    },
    "cbc": {
        "jurisdiction": "ca",
        "name": {
            "en": "Copyright Board of Canada",
            "fr": "Commission du droit d'auteur du Canada",
        },
        "url": {
            "en": "cb",
            "fr": "cda",
        },
        "court_id": ["cb", "cda", "ca cda", "ca cb"],
    },
    "qcoagbrn": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Arbitration - The Guarantee Plan For New Residential Buildings",
        },
        "url": {
            "en": "qcoagbrn",
            "fr": "qcoagbrn",
        },
        "court_id": ["qc oagbrn"],
    },
    "qccdcm": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Collège des médecins du Québec Disciplinary Council",
        },
        "url": {
            "en": "qccdcm",
            "fr": "qccdcm",
        },
        "court_id": ["qc cdcm", "qccdmd"],
    },
    "qcoaq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des acupuncteurs du Québec",
        },
        "url": {
            "en": "qcoaq",
            "fr": "qcoaq",
        },
        "court_id": ["qc oaq", "qccdac"],
    },
    "vrab": {
        "jurisdiction": "ca",
        "name": {
            "en": "Veterans Review and Appeal Board of Canada",
        },
        "url": {
            "en": "vrab",
            "fr": "catacra",
        },
        "court_id": ["ca vrab", "ca tacra"],
    },
    "cbsc-ccnr": {
        "jurisdiction": "ca",
        "name": {
            "en": "Canadian Broadcast Standards Council",
            "fr": "Conseil canadien des normes de la radiotélévision",
        },
        "url": {
            "en": "cbsc",
            "fr": "ccnr",
        },
        "court_id": ["cbsc", "ccnr"],
    },
    "qccja": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de la justice administrative",
        },
        "url": {
            "en": "qccja",
            "fr": "qccja",
        },
        "court_id": ["qc cja"],
    },
    "qccdopq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre des pharmaciens du Québec",
        },
        "url": {
            "en": "qccdopq",
            "fr": "qccdopq",
        },
        "court_id": ["qc cdopq", "qccdpha"],
    },
    "abhraat": {
        "jurisdiction": "ab",
        "name": {
            "en": "Horse Racing Alberta Appeal Tribunal",
        },
        "url": {
            "en": "abhraat",
            "fr": "abhraat",
        },
        "court_id": ["abhraat"],
    },
    "aboipc": {
        "jurisdiction": "ab",
        "name": {
            "en": "Office of the Information and Privacy Commissioner",
        },
        "url": {
            "en": "aboipc",
            "fr": "aboipc",
        },
        "court_id": ["ab oipc"],
    },
    "nlls": {
        "jurisdiction": "nl",
        "name": {
            "en": "Law Society of Newfoundland and Labrador",
        },
        "url": {
            "en": "nlls",
            "fr": "nlls",
        },
        "court_id": ["nl ls"],
    },
    "csc-scc": {
        "jurisdiction": "ca",
        "name": {
            "en": "Supreme Court of Canada",
            "fr": "Cour suprême du Canada",
        },
        "url": {
            "en": "scc",
            "fr": "csc",
        },
        "court_id": ["csc", "scc"],
    },
    "qccdbq": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Barreau du Québec  Disciplinary Council",
        },
        "url": {
            "en": "qccdbq",
            "fr": "qccdbq",
        },
        "court_id": ["qc cdbq", "qccdbq"],
    },
}

# Map citation abbreviations to the database_id

COURT_CODE_MAP = [
    ("nl pc", "nlpc"),
    ("nlpb", "nlpb"),
    ("qccdpod", "qcopodq"),
    ("qc opodq", "qcopodq"),
    ("qc amf", "qcamf"),
    ("abca", "abca"),
    ("altascad", "abca"),
    ("ab ca", "abca"),
    ("bccnm", "bccnm"),
    ("qc cmmtq", "qccmmtq"),
    ("nuwcat", "nuwcat"),
    ("nt wcat", "ntwcat"),
    ("sk ufc", "skufc"),
    ("nbfcst", "nbsec"),
    ("nbsecf", "nbsec"),
    ("oncdho", "oncdho"),
    ("qccdcpa", "qccpa"),
    ("qc cpa", "qccpa"),
    ("on hrt", "onhrt"),
    ("hrto", "onhrt"),
    ("qc tt", "qctt"),
    ("bchprb", "bchprb"),
    ("bc hprb", "bchprb"),
    ("nsawab", "nsawab"),
    ("qccdsf", "qccdosfq"),
    ("qc cdosfq", "qccdosfq"),
    ("bcrmb", "bcrmb"),
    ("bcest", "bcest"),
    ("bc est", "bcest"),
    ("qctp", "qctp"),
    ("qc tp", "qctp"),
    ("lsbc", "lsbc"),
    ("ls bc", "lsbc"),
    ("qccdhj", "qccdhj"),
    ("qc cdhj", "qccdhj"),
    ("sk ipc", "skipc"),
    ("abesab", "abesu"),
    ("ab esa", "abesu"),
    ("cmac", "cmac-cacm"),
    ("cacm", "cmac-cacm"),
    ("oncswssw", "oncswssw"),
    ("qccdcrim", "qccdcrim"),
    ("qc cdcrim", "qccdcrim"),
    ("onbcc", "onbcc"),
    ("on bcc", "onbcc"),
    ("sk ac", "skac"),
    ("nuca", "nuca"),
    ("nu ca", "nuca"),
    ("bc cps", "bccps"),
    ("abrtdrs", "abrtdrs"),
    ("abcpa", "abcpa"),
    ("onsc", "onsc"),
    ("on sc", "onsc"),
    ("nl hrc", "nlhrc"),
    ("nucj", "nucj"),
    ("nu cj", "nucj"),
    ("on sec", "onsec"),
    ("on cvm", "onsec"),
    ("pe ipc", "peipc"),
    ("ns sirt", "nssirt"),
    ("abcpt", "abcpt"),
    ("abpaca", "abcpt"),
    ("on rc", "onrc"),
    ("nbrea", "nbrea"),
    ("ab ci", "abci"),
    ("cm", "cm"),
    ("ca cm", "cm"),
    ("onset", "onset"),
    ("onted", "onset"),
    ("qcrmaaq", "qcrmaaq"),
    ("qc oeq", "qcoeq"),
    ("qccderg", "qcoeq"),
    ("bcca", "bcca"),
    ("bc ca", "bcca"),
    ("qctmf", "qcbdrvm"),
    ("qc tmfqcbdr", "qcbdrvm"),
    ("qcbdrvm", "qcbdrvm"),
    ("eptc", "eptc"),
    ("tpec", "eptc"),
    ("sk fcaa", "sksec"),
    ("fpslreb", "pslreb"),
    ("pslreb", "pslreb"),
    ("crtespf", "pslreb"),
    ("crtefp", "pslreb"),
    ("mbca", "mbca"),
    ("mb ca", "mbca"),
    ("skca", "skca"),
    ("sk ca", "skca"),
    ("qc cdnq", "qccdnq"),
    ("qccdnot", "qccdnq"),
    ("ntwcat", "ntwcat"),
    ("nt wcat", "ntwcat"),
    ("ntnuwcat", "ntwcat"),
    ("nu wcat", "nuwcat"),
    ("onombud", "onombud"),
    ("qcochq", "qcochq"),
    ("qccdchim", "qcochq"),
    ("nwtca", "ntca"),
    ("nwt ca", "ntca"),
    ("on scsm", "onscsm"),
    ("qcctq", "qcctq"),
    ("abesdab", "abesdab"),
    ("ab wcac", "abwcac"),
    ("onoct", "onoct"),
    ("scc", "csc-scc-al"),
    ("csc", "csc-scc-al"),
    ("qcolf", "qcolf"),
    ("mb sec", "mbsec"),
    ("mb cvm", "mbsec"),
    ("onct", "onst"),
    ("qc cdccoq", "qccdccoq"),
    ("qccdco", "qccdccoq"),
    ("onfsc", "onfsc"),
    ("oncsi", "onfsc"),
    ("on fsc", "onfsc"),
    ("sst", "sst-tss"),
    ("sstad", "sst-tss"),
    ("tss", "sst-tss"),
    ("tssda", "sst-tss"),
    ("on carps", "onhparb"),
    ("on hparb", "onhparb"),
    ("sk lrb", "sklrb"),
    ("qc cse", "qccse"),
    ("mbhr", "mbhrc"),
    ("mb hrc", "mbhrc"),
    ("qccsj", "qccsj"),
    ("nsca", "nsca"),
    ("ns ca", "nsca"),
    ("yksm", "yksm"),
    ("pesctd", "pesctd"),
    ("pe sctd", "pesctd"),
    ("pesc", "pesctd"),
    ("yksc", "yksc"),
    ("skdc", "skdc"),
    ("nsbs", "nsbs"),
    ("abelarb", "abelarb"),
    ("skcppdc", "skcp"),
    ("on agc", "onagc"),
    ("sklss", "sklss"),
    ("lss", "sklss"),
    ("sk lss", "sklss"),
    ("qccrt", "qccrt"),
    ("qc crt", "qccrt"),
    ("bcfst", "bcfst"),
    ("on gsb", "ongsb"),
    ("on crg", "ongsb"),
    ("on wsib", "onwsib"),
    ("on cspaat", "onwsib"),
    ("ns prb", "nsprb"),
    ("qc calp", "qccalp"),
    ("nbapab", "nbapab"),
    ("nbcaeu", "nbapab"),
    ("nb caeu", "nbapab"),
    ("nb apab", "nbapab"),
    ("ciro", "ciro-ocri"),
    ("ocri", "ciro-ocri"),
    ("onoepe", "oncece"),
    ("oncece", "oncece"),
    ("ns wcat", "nswcat"),
    ("bcsfi", "bcsfi"),
    ("cfsrb", "oncfsrb"),
    ("pescad", "pescad"),
    ("pe scad", "pescad"),
    ("peca", "pescad"),
    ("pe ca", "pescad"),
    ("abasc", "absec"),
    ("ab sec", "absec"),
    ("oncpd", "oncpd"),
    ("oncpc", "oncpc"),
    ("on cpc", "oncpc"),
    ("ntllb", "ntllb"),
    ("oncpa", "oncpa"),
    ("nsoipc", "nsfoipop"),
    ("ns foipop", "nsfoipop"),
    ("qc otmq", "qcotmq"),
    ("nbca", "nbca"),
    ("nb ca", "nbca"),
    ("on pprb", "onpprb"),
    ("sk atmpa", "skatmpa"),
    ("oncps", "oncps"),
    ("onpsdt", "oncps"),
    ("oncpsd", "oncps"),
    ("on psdt", "oncps"),
    ("oncpo", "oncpo"),
    ("on cpo", "oncpo"),
    ("on lat", "onlat"),
    ("qc otimro", "qcotimro"),
    ("qccdtimroem", "qcotimro"),
    ("qc oagq", "qcoagq"),
    ("qccdag", "qcoagq"),
    ("cirb", "cirb"),
    ("ccri", "cirb"),
    ("yktc", "yktc"),
    ("yk tc", "yktc"),
    ("ykyc", "yktc"),
    ("yk yc", "yktc"),
    ("yttc", "yktc"),
    ("yt tc", "yktc"),
    ("qc opq", "qcopq"),
    ("qccdpsy", "qcopq"),
    ("qc opdq", "qcopdq"),
    ("qccddtp", "qcopdq"),
    ("ab cpsdc", "abcpsdc"),
    ("bc rec", "bcrec"),
    ("nbfcsc", "nbfc"),
    ("oncmt", "oncmt"),
    ("ontmf", "oncmt"),
    ("onsec", "oncmt"),
    ("abls", "abls"),
    ("lsa", "abls"),
    ("onfst", "onfst"),
    ("on fst", "onfst"),
    ("abecarb", "abecarb"),
    ("bclcrb", "bclcrb"),
    ("bc lcrb", "bclcrb"),
    ("chrt", "chrt"),
    ("tcdp", "chrt"),
    ("nu la", "nula"),
    ("yt tlrb", "yttlrb"),
    ("ontlab", "ontlab"),
    ("qc odlq", "qcodlq"),
    ("qccddd", "qcodlq"),
    ("bc la", "bcla"),
    ("qccdooq", "qcooq"),
    ("qc ooq", "qcooq"),
    ("qc ooaq", "qcooaq"),
    ("qccdoaq", "qcooaq"),
    ("yt pslrb", "ytpslrb"),
    ("bchrt", "bchrt"),
    ("bc hrt", "bchrt"),
    ("nboph", "nbcph"),
    ("ahrc", "abhrc"),
    ("ab hrc", "abhrc"),
    ("cact", "cact"),
    ("ct", "cact"),
    ("tc", "cact"),
    ("oncmto", "oncmto"),
    ("cacp", "cacp"),
    ("ca cp", "cacp"),
    ("cacb", "cacp"),
    ("ca cb", "cacp"),
    ("cidphn", "sopf"),
    ("on ert", "onert"),
    ("on te", "onert"),
    ("skaia", "skaia"),
    ("nlcps", "nlcps"),
    ("ca ci", "caci"),
    ("ca ce", "caci"),
    ("on cno", "oncno"),
    ("ca cisr", "cisr"),
    ("ca irb", "cisr"),
    ("qc cvm", "qccvm"),
    ("onfscdrs", "onfscdrs"),
    ("onicdrg", "onfscdrs"),
    ("nsfc", "nsfc"),
    ("ns fc", "nsfc"),
    ("qc cptaq", "qccptaq"),
    ("qccdcrhri", "qccdrhri"),
    ("qc cdrhri", "qccdrhri"),
    ("skmb", "sksmb"),
    ("ablprt", "ablprt"),
    ("nt la", "ntla"),
    ("pec", "pec-ces"),
    ("ces", "pec-ces"),
    ("qcracj", "qcracj"),
    ("qc racj", "qcracj"),
    ("qccsst", "qccsst"),
    ("qc csst", "qccsst"),
    ("qccnesst", "qccnesst"),
    ("onape", "onape"),
    ("on conrb", "onconrb"),
    ("qc ouq", "qcouq"),
    ("qc cdottdq", "qccdottdq"),
    ("abplab", "abplab"),
    ("ab plab", "abplab"),
    ("qc opiq", "qcopiq"),
    ("qcta", "qctacarra"),
    ("qc ta", "qctacarra"),
    ("bcipc", "bcipc"),
    ("bc icp", "bcipc"),
    ("nwttc", "ntyjc"),
    ("nwtsc", "ntyjc"),
    ("tatcf", "tatc"),
    ("tatce", "tatc"),
    ("ca tat", "tatc"),
    ("nslst", "nslst"),
    ("ns lst", "nslst"),
    ("nsohsap", "nsohsap"),
    ("ns ohsap", "nsohsap"),
    ("qc cdchad", "qccdchad"),
    ("nuls", "nuls"),
    ("skrec", "skrec"),
    ("bc cds", "bccds"),
    ("qccdtp", "qcotpq"),
    ("qc otpq", "qcotpq"),
    ("qcca", "qcca"),
    ("qc ca", "qcca"),
    ("sk hrc", "skhrc"),
    ("oic", "oic"),
    ("ci", "oic"),
    ("nslb", "nslb"),
    ("ns lb", "nslb"),
    ("nslrb", "nslb"),
    ("qccm", "qccm"),
    ("qc cm", "qccm"),
    ("nsla", "nsla"),
    ("ns la", "nsla"),
    ("sk mt", "skmt"),
    ("onwsiat", "onwsiat"),
    ("on wsiat", "onwsiat"),
    ("ontaspaat", "onwsiat"),
    ("skhrt", "skhrt"),
    ("sk hrt", "skhrt"),
    ("bcpc", "bcpc"),
    ("bc pc", "bcpc"),
    ("oncrb", "oncrb"),
    ("qccmeq", "qccmeq"),
    ("ca tcce", "citt-tcce"),
    ("ca citt", "citt-tcce"),
    ("abqb", "abqb"),
    ("abkb", "abqb"),
    ("ab qb", "abqb"),
    ("ab kb", "abqb"),
    ("oncot", "oncoto"),
    ("bcseccom", "bcsec"),
    ("qc opgq", "qcopgq"),
    ("yt la", "ytla"),
    ("nb leb", "nbleb"),
    ("nb cte", "nbleb"),
    ("mbls", "mbls"),
    ("mb ls", "mbls"),
    ("mbsb", "mbls"),
    ("ns lrb", "nslrb"),
    ("mb lb", "mblb"),
    ("sk la", "skla"),
    ("abpc", "abpc"),
    ("ab pc", "abpc"),
    ("abcj", "abpc"),
    ("ab cj", "abpc"),
    ("mb la", "mbla"),
    ("nwt ls", "ntls"),
    ("abeab", "abeab"),
    ("oncicb", "oncicb"),
    ("oncivac", "oncicb"),
    ("nb bhr", "nbbihra"),
    ("tpfd", "capsdpt"),
    ("psdpt", "capsdpt"),
    ("nblsb", "nbls"),
    ("onafraat", "onafraat"),
    ("ablerb", "ablerb"),
    ("ab lerb", "ablerb"),
    ("nb la", "nbla"),
    ("pe la", "pela"),
    ("qccdap", "qcoapq"),
    ("qc oapq", "qcoapq"),
    ("bcrb", "bcrb"),
    ("qccai", "qccai"),
    ("qc cai", "qccai"),
    ("qcta", "qctaa"),
    ("qc taa", "qctaa"),
    ("qccdood", "qccdoooq"),
    ("qc cdoooq", "qccdoooq"),
    ("bclrb", "bclrb"),
    ("bc lrb", "bclrb"),
    ("nssec", "nssec"),
    ("ns sec", "nssec"),
    ("on mlt", "onmlc"),
    ("on tmt", "onmlc"),
    ("skpmb", "skpmb"),
    ("qc ottiaq", "qcottiaq"),
    ("ca cer", "cer-rec"),
    ("ca rec", "cer-rec"),
    ("nbombud", "nbomb"),
    ("nb ombud", "nbomb"),
    ("nbomb", "nbomb"),
    ("ca la", "casa-cala"),
    ("ca sa", "casa-cala"),
    ("qctat", "qctat"),
    ("qc tat", "qctat"),
    ("qccq", "qccq"),
    ("qc cq", "qccq"),
    ("qc taq", "qctaq"),
    ("qccs", "qccs"),
    ("qc cs", "qccs"),
    ("oncocoo", "oncocoo"),
    ("on cocoo", "oncocoo"),
    ("qc ct", "qcct"),
    ("tmob", "tmob"),
    ("comc", "tmob"),
    ("qc oaciq", "qcoaciq"),
    ("onmic", "onmic"),
    ("onca", "onca"),
    ("on ca", "onca"),
    ("nspc", "nspc"),
    ("ns pc", "nspc"),
    ("abreca", "abreca"),
    ("ab reca", "abreca"),
    ("oncvo", "oncvo"),
    ("mbqb", "mbqb"),
    ("mb qb", "mbqb"),
    ("mbkb", "mbqb"),
    ("mb kb", "mbqb"),
    ("sctc", "sct-trp"),
    ("trpc", "sct-trp"),
    ("skqb", "skqb"),
    ("sk qb", "skqb"),
    ("skkb", "skqb"),
    ("sk kb", "skqb"),
    ("on arb", "onarb"),
    ("on cref", "onarb"),
    ("alrb", "ablrb"),
    ("ab lrb", "ablrb"),
    ("qc sat", "qcdag"),
    ("qc la", "qcdag"),
    ("peirac", "peirac"),
    ("pe irac", "peirac"),
    ("sk lgb", "sklgb"),
    ("onctcmpao", "onctcmpao"),
    ("bcsp", "bcsp"),
    ("nwt lsb", "ntlsb"),
    ("mbpc", "mbpc"),
    ("mb pc", "mbpc"),
    ("skpc", "skpc"),
    ("sk pc", "skpc"),
    ("bcsc", "bcsc"),
    ("bc sc", "bcsc"),
    ("ab gaa", "abgaa"),
    ("onsc", "onscdc"),
    ("on scdc", "onscdc"),
    ("on cs", "onscdc"),
    ("oncs", "onscdc"),
    ("nwttc", "nttc"),
    ("nwt tc", "nttc"),
    ("qcrbq", "qcrbq"),
    ("qc rbq", "qcrbq"),
    ("nb wcat", "nbwhscc"),
    ("nb taat", "nbwhscc"),
    ("nwtaat", "ntaat"),
    ("onrcdso", "onrcdso"),
    ("on rcdso", "onrcdso"),
    ("sk su", "sksu"),
    ("bcitab", "bcitab"),
    ("nbpc", "nbpc"),
    ("nb pc", "nbpc"),
    ("qc ces", "qcces"),
    ("ondr", "ondr"),
    ("bcorl", "bcorl"),
    ("yk hrc", "ykhrc"),
    ("pe pc", "pepc"),
    ("bcccalab", "bcccalab"),
    ("nlsc", "nlsctd"),
    ("nl sc", "nlsctd"),
    ("nlsctd", "nlsctd"),
    ("nltd", "nlsctd"),
    ("skmbr", "skmbr"),
    ("nwtsc", "ntsc"),
    ("ntsc", "ntsc"),
    ("nwt sc", "ntsc"),
    ("oncrpo", "oncrpo"),
    ("nlca", "nlca"),
    ("nl ca", "nlca"),
    ("nfca", "nlca"),
    ("nwt ro", "ntro"),
    ("nuipc", "nuipc"),
    ("on hrap", "onhrap"),
    ("on cacc", "onhrap"),
    ("oncj", "oncj"),
    ("on cj", "oncj"),
    ("cart", "cart-crac"),
    ("ca art", "cart-crac"),
    ("crac", "cart-crac"),
    ("ca cra", "cart-crac"),
    ("bcfac", "bcfac"),
    ("nspb", "nspr"),
    ("ns pr", "nspr"),
    ("qctadp", "qccdp"),
    ("qc tadp", "qccdp"),
    ("chrc cdp", "qccdp"),
    ("qc tdap", "qccdp"),
    ("qc cdp", "qccdp"),
    ("qccdp", "qccdp"),
    ("onco", "onco"),
    ("ykca", "ykca"),
    ("yk ca", "ykca"),
    ("qctdp", "qctdp"),
    ("qc tdp", "qctdp"),
    ("cq tdp", "qctdp"),
    ("tdp qc", "qctdp"),
    ("tdp cq", "qctdp"),
    ("qc cmnq", "qccmnq"),
    ("qccdoppq", "qcoppq"),
    ("qc oppq", "qcoppq"),
    ("qccdinf", "qccdoii"),
    ("qc cdoii", "qccdoii"),
    ("ntipc", "ntipc"),
    ("nwt ipc", "ntipc"),
    ("qc oarq", "qcoarq"),
    ("qccdarc", "qcoarq"),
    ("mbcpsdc", "mbcpsdc"),
    ("forep", "forep"),
    ("nssc", "nssc"),
    ("ns sc", "nssc"),
    ("nssf", "nssf"),
    ("ns sf", "nssf"),
    ("nssm", "nssm"),
    ("onnfppb", "onnfppb"),
    ("ab sdab", "absdab"),
    ("cgysdab", "absdab"),
    ("bceab", "bceab"),
    ("nbqb", "nbqb"),
    ("nbkb", "nbqb"),
    ("nbbr", "nbqb"),
    ("nb qb", "nbqb"),
    ("nb kb", "nbqb"),
    ("nb br", "nbqb"),
    ("ns hrc", "nshrc"),
    ("qc oiia", "qccdoiia"),
    ("qccdia", "qccdoiia"),
    ("mb hab", "mbhab"),
    ("qc craaap", "qccraaap"),
    ("craaap", "qccraaap"),
    ("on lrb", "onlrb"),
    ("qccdcsf", "qccdcsf"),
    ("qc cdcsf", "qccdcsf"),
    ("abohsab", "abohsab"),
    ("skort", "skort"),
    ("yjcn", "nuyc"),
    ("oncaspd", "oncaspd"),
    ("bc wcat", "bcwcat"),
    ("bcogat", "bcogat"),
    ("qc cdoiq", "qccdoiq"),
    ("qccding", "qccdoiq"),
    ("nt tadp", "nthrap"),
    ("nt hrap", "nthrap"),
    ("bchab", "bchab"),
    ("uk jcpc", "ukpc"),
    ("nsuarb", "nsuarb"),
    ("qccdhd", "qcohdq"),
    ("qc ohdq", "qcohdq"),
    ("fca", "fca"),
    ("caf", "fca"),
    ("qc rde", "qcrde"),
    ("camfda", "camfda"),
    ("ca accfm", "camfda"),
    ("ca mfdac", "camfda"),
    ("qc oifq", "qcoifq"),
    ("qccdingf", "qcoifq"),
    ("qc tal", "qcrdl"),
    ("qctal", "qcrdl"),
    ("fct", "fct"),
    ("fc", "fct"),
    ("cf", "fct"),
    ("nllrb", "nllrb"),
    ("nl lrb", "nllrb"),
    ("pssrb", "pssrb"),
    ("crtfp", "pssrb"),
    ("pslrb", "pssrb"),
    ("sk fca", "skfca"),
    ("qccdsexo", "qcopsq"),
    ("qc opsq", "qcopsq"),
    ("nu sec", "nusec"),
    ("qccfp", "qccfp"),
    ("qc cfp", "qccfp"),
    ("qc mff", "qccfp"),
    ("qc psc", "qccfp"),
    ("nl la", "nlla"),
    ("on lpat", "onmb"),
    ("on taal", "onmb"),
    ("iroc", "caiiroc"),
    ("ocrcvm", "caiiroc"),
    ("ca ocrcvm", "caiiroc"),
    ("ca iiroc", "caiiroc"),
    ("iiroc", "caiiroc"),
    ("ns cps", "nscps"),
    ("abtsb", "abtsb"),
    ("onsbt", "onsbt"),
    ("ca céc", "exchc-cech"),
    ("ca exc", "exchc-cech"),
    ("on ccb", "onccb"),
    ("ccic", "iccrc"),
    ("cicc", "iccrc"),
    ("iccrc", "iccrc"),
    ("crcic", "iccrc"),
    ("on peht", "onpeht"),
    ("qccdodq", "qcodq"),
    ("qc odq", "qcodq"),
    ("ablcb", "ablcb"),
    ("ab lcb", "ablcb"),
    ("psst", "psst"),
    ("tdfp", "psst"),
    ("on ipc", "onipc"),
    ("on lt", "onlt"),
    ("qc cm", "qccmq"),
    ("onacrb", "onacrb"),
    ("on acrb", "onacrb"),
    ("on cesa", "onacrb"),
    ("oncesa", "onacrb"),
    ("bcsre", "bcsre"),
    ("bccrt", "bccrt"),
    ("qcadmaq", "qcadmaq"),
    ("qccdadma", "qcadmaq"),
    ("qc admaq", "qcadmaq"),
    ("on hsarb", "onhsarb"),
    ("oncarss", "onhsarb"),
    ("on la", "onla"),
    ("bcctc", "bcctc"),
    ("absra", "absra"),
    ("pcc", "pcc-cvpc"),
    ("cvpc", "pcc-cvpc"),
    ("absrb", "absrb"),
    ("qc ocq", "qcocq"),
    ("qccdchir", "qcocq"),
    ("qc cdppq", "qccdppq"),
    ("qccdpsed", "qccdppq"),
    ("ytrto", "ytrto"),
    ("oncpdc", "oncpdc"),
    ("qcclp", "qcclp"),
    ("qc clp", "qcclp"),
    ("abcgyarb", "abcgyarb"),
    ("ab cgyarb", "abcgyarb"),
    ("qccdmv", "qccdomv"),
    ("qc cdomv", "qccdomv"),
    ("onlsta", "onlst"),
    ("onlsap", "onlst"),
    ("onlsth", "onlst"),
    ("ontbh", "onlst"),
    ("on lst", "onlst"),
    ("onlshp", "onlst"),
    ("abmgb", "abmgb"),
    ("cci", "cci-tcc"),
    ("tcc", "cci-tcc"),
    ("nhrt", "nuhrt"),
    ("qc otstcfq", "qcotstcfq"),
    ("qccdtstcf", "qcotstcfq"),
    ("on psgb", "onpsgb"),
    ("on cgfp", "onpsgb"),
    ("onltb", "onltb"),
    ("on ltb", "onltb"),
    ("oncat", "oncat"),
    ("ontasc", "oncat"),
    ("pe hrc", "peihrc"),
    ("pe lrb", "pelrb"),
    ("nl ipc", "nlipc"),
    ("qc agq", "qcagq"),
    ("qccdagr", "qcagq"),
    ("qc oeaq", "qcoeaq"),
    ("qccdea", "qcoeaq"),
    ("ablcsab", "ablcsab"),
    ("ohstc", "ohstc"),
    ("tsstc", "ohstc"),
    ("cb", "cbc"),
    ("cda", "cbc"),
    ("ca cda", "cbc"),
    ("ca cb", "cbc"),
    ("qc oagbrn", "qcoagbrn"),
    ("qc cdcm", "qccdcm"),
    ("qccdmd", "qccdcm"),
    ("qc oaq", "qcoaq"),
    ("qccdac", "qcoaq"),
    ("ca vrab", "vrab"),
    ("ca tacra", "vrab"),
    ("cbsc", "cbsc-ccnr"),
    ("ccnr", "cbsc-ccnr"),
    ("qc cja", "qccja"),
    ("qc cdopq", "qccdopq"),
    ("qccdpha", "qccdopq"),
    ("abhraat", "abhraat"),
    ("ab oipc", "aboipc"),
    ("nl ls", "nlls"),
    ("csc", "csc-scc"),
    ("scc", "csc-scc"),
    ("qc cdbq", "qccdbq"),
    ("qccdbq", "qccdbq"),
]
