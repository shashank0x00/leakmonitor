import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (LeakHunter-Bot)"
}

def search_duckduckgo(domain):
    query = f'site:pastebin.com "{domain}"'
    url = f"https://html.duckduckgo.com/html/?q={query}"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    return list(set(a['href'] for a in soup.find_all("a", href=True) if "pastebin.com" in a['href']))