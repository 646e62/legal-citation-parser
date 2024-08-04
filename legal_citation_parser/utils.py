# utils.py

import requests
import os
import sys
import sqlite3
from dotenv import load_dotenv, set_key, find_dotenv

class Utility:
    @staticmethod
    def check_url(url):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return url
            else:
                return None
        except requests.RequestException:
            return None

    @staticmethod
    def set_api_key_env_var():
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)

        if os.getenv("CANLII_API_KEY") is None:
            print("The citation parser can provide additional functionality for users with access to the CanLII API.\n", 
                  "Enter your CanLII API key to enable or ENTER (blank input) to skip/remove:")
            API_KEY = input().strip()
            if API_KEY == "":
                sys.exit("No API key entered. Exiting.")
            else:
                os.environ['CANLII_API_KEY'] = API_KEY
                if dotenv_path:
                    set_key(dotenv_path, "CANLII_API_KEY", API_KEY)
                else:
                    with open('.env', 'w') as env_file:
                        env_file.write(f"CANLII_API_KEY={API_KEY}\n")
                print("API key has been set and saved to the .env file.")
        else:
            API_KEY = os.getenv("CANLII_API_KEY")
            print("API key loaded from environment variable.")

        return API_KEY

class CanLIIAPI:
    @staticmethod
    def check_for_api_error_codes(response):
        if "error" in response:
            return True
        return False

    @staticmethod
    def api_call(case_id=None, database_id=None, language="en", decision_metadata=False, cases_cited=False, cases_citing=False, canlii_database=False):
        load_dotenv()
        if os.getenv("CANLII_API_KEY") is None:
            API_KEY = Utility.set_api_key_env_var()
            if API_KEY == "":
                sys.exit()
        else:
            API_KEY = os.getenv("CANLII_API_KEY")

        metadata_api_info = {}

        if decision_metadata:
            metadata_url = f"https://api.canlii.org/v1/caseBrowse/{language}/{database_id}/{case_id}/?api_key={API_KEY}"
            response = requests.get(metadata_url, timeout=5)
            case_metadata = response.json()
            if type(case_metadata) == list and CanLIIAPI.check_for_api_error_codes(case_metadata[0]):
                return case_metadata
            metadata_api_info["short_url"] = case_metadata["url"]
            metadata_api_info["language"] = case_metadata["language"]
            metadata_api_info["docket_number"] = case_metadata["docketNumber"]
            metadata_api_info["decision_date"] = case_metadata["decisionDate"]
            metadata_api_info["keywords"] = case_metadata.get("keywords", "").split(" — ") if case_metadata.get("keywords") else []
            metadata_api_info["categories"] = case_metadata.get("topics", "").split(" — ") if case_metadata.get("topics") else []

        if cases_cited:
            cited_cases_url = f"https://api.canlii.org/v1/caseCitator/{language}/{database_id}/{case_id}/citedCases?api_key={API_KEY}"
            response = requests.get(cited_cases_url, timeout=5)
            cited_cases = response.json()
            if type(cited_cases) == list and CanLIIAPI.check_for_api_error_codes(cited_cases):
                return cited_cases
            metadata_api_info["cited_cases"] = cited_cases

        if cases_citing:
            citing_cases_url = f"https://api.canlii.org/v1/caseCitator/{language}/{database_id}/{case_id}/citingCases?api_key={API_KEY}"
            response = requests.get(citing_cases_url, timeout=5)
            citing_cases = response.json()
            if type(citing_cases) == list and CanLIIAPI.check_for_api_error_codes(citing_cases):
                return citing_cases
            metadata_api_info["citing_cases"] = citing_cases

        if canlii_database:
            database_url = f"https://api.canlii.org/v1/caseBrowse/{language}/?api_key={API_KEY}"
            response = requests.get(database_url, timeout=5)
            database_info = response.json()
            if type(database_info) == list and CanLIIAPI.check_for_api_error_codes(database_info):
                return database_info
            metadata_api_info["database"] = database_info

        return metadata_api_info

class DatabaseManager:
    @staticmethod
    def create_citation_database():
        conn = sqlite3.connect('results.db')
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS results (
                uid TEXT PRIMARY KEY,
                style_of_cause TEXT,
                atomic_citation TEXT,
                citation_type TEXT,
                scr_citation TEXT,
                year TEXT,
                court TEXT,
                decision_number TEXT,
                jurisdiction TEXT,
                court_name TEXT,
                court_level TEXT,
                long_url TEXT,
                short_url TEXT,
                language TEXT,
                docket_number TEXT,
                decision_date TEXT
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS keywords (
                uid TEXT,
                keyword TEXT,
                FOREIGN KEY (uid) REFERENCES results (uid)
            )
        ''')

        c.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                uid TEXT,
                category TEXT,
                FOREIGN KEY (uid) REFERENCES results (uid)
            )
        ''')

        conn.commit()
        conn.close()

    @staticmethod
    def insert_data(data, update_existing=False):
        conn = sqlite3.connect('results.db')
        c = conn.cursor()

        if update_existing:
            c.execute('''
                INSERT INTO results (uid, style_of_cause, atomic_citation, citation_type, scr_citation, 
                                     year, court, decision_number, jurisdiction, court_name, court_level,
                                     long_url, short_url, language, docket_number, decision_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(uid) DO UPDATE SET
                style_of_cause=excluded.style_of_cause, atomic_citation=excluded.atomic_citation, citation_type=excluded.citation_type, 
                scr_citation=excluded.scr_citation, year=excluded.year, court=excluded.court, 
                decision_number=excluded.decision_number, jurisdiction=excluded.jurisdiction, 
                court_name=excluded.court_name, court_level=excluded.court_level, long_url=excluded.long_url, 
                short_url=excluded.short_url, language=excluded.language, docket_number=excluded.docket_number, 
                decision_date=excluded.decision_date
            ''', (data['uid'], data['style_of_cause'], data['atomic_citation'], data['citation_type'], data['scr_citation'],
                  data['year'], data['court'], data['decision_number'], data['jurisdiction'], data['court_name'], data['court_level'],
                  data['long_url'], data['short_url'], data['language'], data['docket_number'], data['decision_date']))
        else:
            c.execute('''
                INSERT OR IGNORE INTO results (uid, style_of_cause, atomic_citation, citation_type, scr_citation, 
                                              year, court, decision_number, jurisdiction, court_name, court_level,
                                              long_url, short_url, language, docket_number, decision_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (data['uid'], data['style_of_cause'], data['atomic_citation'], data['citation_type'], data['scr_citation'],
                  data['year'], data['court'], data['decision_number'], data['jurisdiction'], data['court_name'], data['court_level'],
                  data['long_url'], data['short_url'], data['language'], data['docket_number'], data['decision_date']))

        if data.get('keywords'):
            keywords = data['keywords'].split(' — ')
            for keyword in keywords:
                c.execute('INSERT OR IGNORE INTO keywords (uid, keyword) VALUES (?, ?)', (data['uid'], keyword))

        if data.get('categories'):
            categories = data['categories'].split(' — ')
            for category in categories:
                c.execute('INSERT OR IGNORE INTO categories (uid, category) VALUES (?, ?)', (data['uid'], category))

        conn.commit()
        conn.close()
