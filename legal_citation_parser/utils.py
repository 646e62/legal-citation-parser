# utils.py

import requests
import os
import sys
import time
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
            API_KEY = CanLIIAPI.set_api_key()
            if API_KEY == "":
                sys.exit()
        else:
            API_KEY = os.getenv("CANLII_API_KEY")

        metadata_api_info = {}

        if decision_metadata:
            time.sleep(0.5)  # Introduce a 2-second delay to avoid rate limiting
            metadata_url = f"https://api.canlii.org/v1/caseBrowse/{language}/{database_id}/{case_id}/?api_key={API_KEY}"
            response = requests.get(metadata_url, timeout=5)
            case_metadata = response.json()

            if type(case_metadata) == list and CanLIIAPI.check_for_api_error_codes(case_metadata[0]):
                metadata_api_info["error"] = case_metadata[0]["message"]
                return metadata_api_info
            
            metadata_api_info["short_url"] = case_metadata["url"]
            metadata_api_info["language"] = case_metadata["language"]
            metadata_api_info["docket_number"] = case_metadata["docketNumber"]
            metadata_api_info["decision_date"] = case_metadata["decisionDate"]
            metadata_api_info["keywords"] = case_metadata.get("keywords", "").split(" — ") if case_metadata.get("keywords") else []
            metadata_api_info["categories"] = case_metadata.get("topics", "").split(" — ") if case_metadata.get("topics") else []

        if cases_cited:
            time.sleep(0.5)
            cited_cases_url = f"https://api.canlii.org/v1/caseCitator/{language}/{database_id}/{case_id}/citedCases?api_key={API_KEY}"
            response = requests.get(cited_cases_url, timeout=5)
            cited_cases = response.json()

            if type(cited_cases) == list and CanLIIAPI.check_for_api_error_codes(cited_cases):
                metadata_api_info["error"] = cited_cases[0]["message"]
                return cited_cases
            
            metadata_api_info["cited_cases"] = cited_cases

        if cases_citing:
            time.sleep(0.5)
            citing_cases_url = f"https://api.canlii.org/v1/caseCitator/{language}/{database_id}/{case_id}/citingCases?api_key={API_KEY}"
            response = requests.get(citing_cases_url, timeout=5)
            citing_cases = response.json()

            if type(citing_cases) == list and CanLIIAPI.check_for_api_error_codes(citing_cases):
                metadata_api_info["error"] = citing_cases[0]["message"]
                return citing_cases
            
            metadata_api_info["citing_cases"] = citing_cases

        if canlii_database:
            time.sleep(0.5)
            database_url = f"https://api.canlii.org/v1/caseBrowse/{language}/?api_key={API_KEY}"
            response = requests.get(database_url, timeout=5)
            database_info = response.json()

            if type(database_info) == list and CanLIIAPI.check_for_api_error_codes(database_info):
                metadata_api_info["error"] = database_info[0]["message"]
                return database_info
            
            metadata_api_info["database"] = database_info

        return metadata_api_info


    @staticmethod
    def set_api_key(api_key: str = None, force_overwrite=False, force_delete=False):
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)

        if api_key:
            current_api_key = api_key
        else:
            current_api_key = os.getenv("CANLII_API_KEY")
        
        if force_delete:
            if current_api_key:
                os.environ.pop("CANLII_API_KEY")
                if dotenv_path:
                    set_key(dotenv_path, "CANLII_API_KEY", "")
                print("API key has been removed.")
            else:
                print("No API key found to remove.")
            return None

        if force_overwrite:
            print("Forced overwrite of the API key.")
            API_KEY = CanLIIAPI.prompt_for_api_key()
            CanLIIAPI.save_api_key(dotenv_path, API_KEY)
            return API_KEY

        if current_api_key is None:
            print("No API key found. Please enter your CanLII API key:")
            API_KEY = input().strip()
            if API_KEY == "":
                sys.exit("No API key entered. Exiting.")
            CanLIIAPI.save_api_key(dotenv_path, API_KEY)
        else:
            print(f"Current API key: {current_api_key}")
            print("Would you like to overwrite it? (yes to overwrite, no to keep, enter to remove)")
            user_input = input().strip().lower()
            if user_input == "yes":
                API_KEY = CanLIIAPI.prompt_for_api_key()
                CanLIIAPI.save_api_key(dotenv_path, API_KEY)
            elif user_input == "":
                print("Removing the existing API key.")
                os.environ.pop("CANLII_API_KEY")
                if dotenv_path:
                    set_key(dotenv_path, "CANLII_API_KEY", "")
                print("API key has been removed.")
                return None
            else:
                print("Keeping the existing API key.")
                API_KEY = current_api_key

        return API_KEY

    @staticmethod
    def prompt_for_api_key():
        print("Enter your CanLII API key:")
        API_KEY = input().strip()
        if API_KEY == "":
            sys.exit("No API key entered. Exiting.")
        return API_KEY

    @staticmethod
    def save_api_key(dotenv_path, API_KEY):
        os.environ['CANLII_API_KEY'] = API_KEY
        if dotenv_path:
            set_key(dotenv_path, "CANLII_API_KEY", API_KEY)
        else:
            with open('.env', 'w') as env_file:
                env_file.write(f"CANLII_API_KEY={API_KEY}\n")
        print("API key has been set and saved to the .env file.")

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
