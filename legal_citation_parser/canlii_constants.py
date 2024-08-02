"""
Contains constants that map court names to their respective levels and jurisdictions.
"""

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
        "court_type": "provincial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_id": ["nuwcat", "ntwcat", "nt wcat", "ntnuwcat"],
        "court_type": "territorial tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "military appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_id": ["cm", "ca cm"],
        "court_type": "military",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial appellate",
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
        "court_id": ["qctmf", "qc tmf", "qcbdr", "qcbdrvm"],
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
    },
    "fpca": {
        "jurisdiction": "ca",
        "name": {
            "en": "FP Canada Standards Council",
            "fr": "FP Canada Standards Council",
        },
        "url": {
            "en": "fpca",
            "fr": "fpca",
        },
        "court_id": ["fpca"],
        "court_type": "federal tribunal",
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
        "court_type": "provincial appellate",
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
        "court_type": "provincial appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial appellate",
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
        "court_type": "territorial tribunal",
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
        "court_type": "superior",
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
        "court_type": "superior",
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
        "court_type": "provincial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "territorial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_id": ["nbcph"],
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
    },
    "qccdrhri": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Conseil de discipline de l'Ordre professionnel des conseillers en ressources humaines et en relations industrielles agrées du Québec",
        },
        "url": {"en": "qccdrhri"},
        "court_id": ["qccdcrhri", "qc cdrhri"],
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
    },
    "qccnesst": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission des normes, de l’équité, de la santé et de la sécurité du travail",
        },
        "url": {"en": "qccnesst"},
        "court_id": ["qccnesst"],
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
    },
    "ntyjc": {
        "jurisdiction": "nt",
        "name": {
            "en": "Youth Justice Court",
        },
        "url": {"en": "ntyjc"},
        "court_id": ["nwttc", "nwtsc"],
        "court_type": "territorial",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial appellate",
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
        "court_type": "provincial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "superior",
    },
    "sct-trp": {
        "jurisdiction": "ca",
        "name": {
            "en": "Specific Claims Tribunal Canada",
            "fr": "Tribunal des revendications particulières Canada",
        },
        "url": {
            "en": "sct",
            "fr": "trp",
        },
        "court_id": ["sctc", "trpc"],
        "court_type": "federal tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_id": ["nwt lsb", "ntesa"],
        "court_type": "territorial tribunal",
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
        "court_type": "provincial",
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
        "court_type": "provincial",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "superior",
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
        "court_id": ["nwttc", "nwt tc", "nwttc"],
        "court_type": "territorial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_id": ["nwtsc", "ntsc", "nwt sc", "nwtsc"],
        "court_type": "territorial",
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
        "court_id": ["oncrpo", "onrpdt"],
        "court_type": "provincial tribunal",
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
        "court_type": "provincial appellate",
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
        "court_type": "territorial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_id": ["mbcpsdc", "mb cpsdc"],
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "superior",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "superior",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
    },
    "bcogat": {
        "jurisdiction": "bc",
        "name": {
            "en": "Oil and Gas Appeal Tribunal",
        },
        "url": {
            "en": "bcogat",
            "fr": "bcogat",
        },
        "court_id": ["bcogat"],
        "court_type": "provincial tribunal",
    },
    "bcerat": {
        "jurisdiction": "bc",
        "name": {
            "en": "Energy Resource Appeal Tribunal",
        },
        "url": {
            "en": "bcerat",
            "fr": "bcerat",
        },
        "court_id": ["bcerat"],
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal appellate",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
    },
    "qccfp": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Commission de la fonction publique",
        },
        "url": {"en": "qccfp"},
        "court_id": ["qccfp", "qc cfp", "qc mff", "qc psc"],
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal",
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
        "court_type": "territorial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "federal tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "provincial tribunal",
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
        "court_type": "federal appellate",
    },
    "qccdbq": {
        "jurisdiction": "qc",
        "name": {
            "en": "Barreau du Québec Disciplinary Council",
            "fr": "Conseil de discipline du Barreau du Québec"
        },
        "url": {
            "en": "qccdbq",
            "fr": "qccdbq",
        },
        "court_id": ["qc cdbq", "qccdbq"],
        "court_type": "provincial tribunal",
    },
    "sopf": {
        "jurisdiction": "ca",
        "name": {
            "en": "Ship-source Oil Pollution Fund",
            "fr": "Caisse d'indemnisation des dommages dus à la pollution par les hydrocarbures causée par les navires",
        },
        "url": {
            "en": "sopf",
            "fr": "cidphn",
        },
        "court_id": ["sopf", "cidphn"],
        "court_type": "federal tribunal",
    },
    "bcegbc": {
        "jurisdiction": "bc",
        "name": {
            "en": "Engineers and Geoscientists British Columbia",
        },
        "url": {
            "en": "bcegbc",
            "fr": "bcegbc",
        },
        "court_id": ["bcegbc", "bceg"],
        "court_type": "provincial tribunal",
    },
    "ntsec": {
        "jurisdiction": "nt",
        "name": {
            "en": "Northwest Territories Securities Office",
            "fr": "Northwest Territories Securities Office",
        },
        "url": {
            "en": "ntsec",
            "fr": "ntsec",
        },
        "court_id": ["nt sec", "ntsec"],
        "court_type": "territorial tribunal",
    },
    "ntydab": { 
        "jurisdiction": "nt",
        "name": {
            "en": "Yellowknife Development Appeal Board",
        },
        "url": {
            "en": "ntydab",
            "fr": "ntydab",
        },
        "court_id": ["nt ydab", "ntydab"],
        "court_type": "territorial tribunal",
    },
    "qcamp": {
        "jurisdiction": "qc",
        "name": {
            "fr": "Autorité des marchés publics",
        },
        "url": {
            "en": "qcamp",
            "fr": "qcamp",
        },
        "court_id": ["qc amp", "qcamp"],
        "court_type": "provincial tribunal",
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
    ("fpca", "fpca"),
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
    ("scc-l", "csc-scc-al"),
    ("csc-a", "csc-scc-al"),
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
    ("nbcph", "nbcph"),
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
    ("nwttc", "nttc"),
    ("nwtsc", "ntsc"),
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
    ("ntesa", "ntlsb"),
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
    ("onrpdt", "oncrpo"),
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
    ("mb cpsdc", "mbcpsdc"),
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
    ["bcerat", "bcogat"],
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
    ("sopf", "sopf"),
    ("cidphn", "sopf"),
    ("bcegbc", "bcegbc"),
    ("bceg", "bcegbc"),
    ("nt sec", "ntsec"),
    ("nt ydab", "ntydab"),
    ("qc amp", "qcamp"),
    ("qcamp", "qcamp"),
]
