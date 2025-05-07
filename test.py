from serpapi import GoogleSearch

params = {
    "engine": "google_scholar",
    "q": "quantum computing",
    "api_key": "your_serpapi_key_here"
}

search = GoogleSearch(params)
results = search.get_dict()
print(results)

