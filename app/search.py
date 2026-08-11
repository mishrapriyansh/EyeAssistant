from ddgs import DDGS
from app.config import SAFE_SEARCH,MAX_RESULTS
def search(query,domains_list=None):
    try:
        if domains_list:
            domain_filter = " OR ".join([f"site:{domain}" for domain in domains_list])
            query = f"{query} ({domain_filter})"   
        results = DDGS().text(
            query=query,
            safesearch=SAFE_SEARCH,
            max_results=MAX_RESULTS
           )
        return list(results)
    except Exception as e:
        print(f"Error during search: {e}")
        return []

