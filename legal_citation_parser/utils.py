"""
Shared utility functions for the legal citation parser.
"""

import requests
import os
import sys
import requests
import sqlite3

from dotenv import load_dotenv

def check_url(url: str) -> str:
    """
    Checks if a URL is valid by sending a GET request and verifying the status code.

    Args:
        url (str): The URL to check.

    Returns:
        str: The URL if it is valid, otherwise None.
    """

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return url
        else:
            return None
    except requests.RequestException:
        return None


def canlii_api_call(
    case_id: str = None,
    database_id: str = None,
    legislation_id: str = None,
    language: str = "en",
    decision_metadata=False,
    legislation_metadata=False,
    cases_cited=False,
    cases_citing=False,
    canlii_database=False,
) -> dict:
    """
    Makes an API call to the CanLII API to retrieve metadata information about a case.

    Args:
        case_id (str): The unique CanLII case ID.

    Returns:
        dict: A dictionary containing the metadata information about the case, including the style
        of cause, citation, citation type (neutral or CanLII), year, court code, decision number,
        jurisdiction, court name, and court level. The dictionary will also include the CanLII URL.
    """

    """
    if os.getenv("CANLII_API_KEY") is None:
        print("Please enter your CanLII API key (or blank input to exit):")
        API_KEY = input()
        if API_KEY == "":
            sys.exit()
    """

    load_dotenv()
    if os.getenv("CANLII_API_KEY") is None:
        API_KEY = set_canlii_api_key_env_var()
        if API_KEY == "":
            sys.exit()
    else:
        API_KEY = os.getenv("CANLII_API_KEY")

    metadata_api_info = {}

    if decision_metadata:
        metadata_url = f"https://api.canlii.org/v1/caseBrowse/{language}/{database_id}/{case_id}/?api_key={API_KEY}"
        response = requests.get(metadata_url, timeout=5)
        case_metadata = response.json()
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
        metadata_api_info["cited_cases"] = cited_cases

    if cases_citing:
        citing_cases_url = f"https://api.canlii.org/v1/caseCitator/{language}/{database_id}/{case_id}/citingCases?api_key={API_KEY}"
        response = requests.get(citing_cases_url, timeout=5)
        citing_cases = response.json()
        metadata_api_info["citing_cases"] = citing_cases

    # Placeholder for legislation metadata
    if legislation_metadata:
        metadata_url = f"https://api.canlii.org/v1/legislationBrowse/{language}/{database_id}/{legislation_id}/?api_key={API_KEY}"
        response = requests.get(metadata_url, timeout=5)
        legislation_metadata = response.json()
        metadata_api_info["database_id"] = legislation_metadata["databaseId"]
        metadata_api_info["legislation_id"] = legislation_metadata["legislationId"]
        metadata_api_info["title"] = legislation_metadata["title"]
        metadata_api_info["type"] = legislation_metadata["type"]
        metadata_api_info["citation"] = legislation_metadata["citation"]

    if canlii_database:
        database_url = f"https://api.canlii.org/v1/caseBrowse/{language}/?api_key={API_KEY}"
        response = requests.get(database_url, timeout=5)
        database_info = response.json()
        metadata_api_info["database"] = database_info

    return metadata_api_info


def create_citation_database():
    conn = sqlite3.connect('results.db')
    c = conn.cursor()

    # Create the main results table
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

    # Create the keywords table
    c.execute('''
        CREATE TABLE IF NOT EXISTS keywords (
            uid TEXT,
            keyword TEXT,
            FOREIGN KEY (uid) REFERENCES results (uid)
        )
    ''')

    # Create the categories table
    c.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            uid TEXT,
            category TEXT,
            FOREIGN KEY (uid) REFERENCES results (uid)
        )
    ''')

    conn.commit()
    conn.close()

import sqlite3

def insert_data(data, update_existing=False):
    conn = sqlite3.connect('results.db')
    c = conn.cursor()

    if update_existing:
        # Update existing records if the uid already exists
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
        # Ignore the insert if the uid already exists
        c.execute('''
            INSERT OR IGNORE INTO results (uid, style_of_cause, atomic_citation, citation_type, scr_citation, 
                                          year, court, decision_number, jurisdiction, court_name, court_level,
                                          long_url, short_url, language, docket_number, decision_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data['uid'], data['style_of_cause'], data['atomic_citation'], data['citation_type'], data['scr_citation'],
              data['year'], data['court'], data['decision_number'], data['jurisdiction'], data['court_name'], data['court_level'],
              data['long_url'], data['short_url'], data['language'], data['docket_number'], data['decision_date']))

    # Handle keywords and categories, assuming they need to be unique per uid
    if data.get('keywords'):
        keywords = data['keywords'].split(' — ')  # Assuming keywords are separated by ' — '
        for keyword in keywords:
            c.execute('INSERT OR IGNORE INTO keywords (uid, keyword) VALUES (?, ?)', (data['uid'], keyword))

    if data.get('categories'):
        categories = data['categories'].split(' — ')  # Assuming categories are separated by ' — '
        for category in categories:
            c.execute('INSERT OR IGNORE INTO categories (uid, category) VALUES (?, ?)', (data['uid'], category))

    conn.commit()
    conn.close()

import os
import sys
from dotenv import load_dotenv, set_key, find_dotenv

def set_api_key_env_var():
    """
    Prompts the user to enter an API key and sets it as an environment variable.
    It saves the environment variable to a .env file for persistence across sessions.
    """
    # Load existing environment variables from .env file if available
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    # Check if API key is already set
    if os.getenv("CANLII_API_KEY") is None:
        print("Please enter your CanLII API key (blank input to exit):")
        API_KEY = input().strip()
        if API_KEY == "":
            sys.exit("No API key entered. Exiting.")
        else:
            # Set the environment variable for the current session
            os.environ['CANLII_API_KEY'] = API_KEY
            
            # Save the API key to the .env file for persistence
            if dotenv_path:
                set_key(dotenv_path, "CANLII_API_KEY", API_KEY)
            else:
                # Create a new .env file if it doesn't exist
                with open('.env', 'w') as env_file:
                    env_file.write(f"CANLII_API_KEY={API_KEY}\n")
            print("API key has been set and saved to the .env file.")
    else:
        API_KEY = os.getenv("CANLII_API_KEY")
        print("API key loaded from environment variable.")

    return API_KEY

# Example usage
set_api_key_env_var()
