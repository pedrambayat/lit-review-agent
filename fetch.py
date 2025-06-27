import requests

def fetch_papers(query, limit=3):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": limit,
        "fields": "title,abstract"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return [
        {"title": paper["title"], "abstract": paper.get("abstract", "")}
        for paper in data.get("data", [])
        if paper.get("abstract")
    ]
