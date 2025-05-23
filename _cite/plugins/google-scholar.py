import os
import re
from serpapi import Client
from util import *

def main(entry):
    """
    receives single list entry from google-scholar data file
    returns list of sources to cite
    """
    # get api key (serp api key to access google scholar)
    api_key = os.environ.get("GOOGLE_SCHOLAR_API_KEY", "")
    if not api_key:
        raise Exception('No "GOOGLE_SCHOLAR_API_KEY" env var')
    
    # create serpapi client
    client = Client(api_key=api_key)
    
    # get id from entry
    _id = get_safe(entry, "gsid", "")
    if not _id:
        raise Exception('No "gsid" key')
    
    # query api
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query(_id):
        params = {
            "engine": "google_scholar_author",
            "author_id": _id,
            "num": 100,  # max allowed
        }
        response = client.search(params)
        return get_safe(response, "articles", [])
    
    response = query(_id)
    
    # list of sources to return
    sources = []
    
    # go through response and format sources
    for work in response:
        # Try to extract DOI from the link or other fields
        link = get_safe(work, "link", "")
        doi = extract_doi(link)
        
        # create source
        year = get_safe(work, "year", "")
        source = {
            "id": doi if doi else get_safe(work, "citation_id", ""),
            "title": get_safe(work, "title", ""),
            "authors": list(map(str.strip, get_safe(work, "authors", "").split(","))),
            "publisher": get_safe(work, "publication", ""),
            "date": (year + "-01-01") if year else "",
            "link": link,
            "type": "doi" if doi else "custom",  # Add type for Manubot to know how to handle
        }
        # copy fields from entry to source
        source.update(entry)
        # add source to list
        sources.append(source)
    
    return sources

def extract_doi(text):
    """Try to extract a DOI from text"""
    if not text:
        return ""
    # Look for DOI patterns like 10.xxxx/xxxxx
    doi_match = re.search(r'10\.\d{4,}[\w\.\-\/]+', text)
    if doi_match:
        return doi_match.group(0)
    return ""
