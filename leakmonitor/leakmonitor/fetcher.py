import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (LeakHunter-Bot)"
}

def fetch_raw_paste(paste_url):
    raw_url = paste_url.replace("pastebin.com/", "pastebin.com/raw/")
    try:
        content = requests.get(raw_url, headers=HEADERS, timeout=10).text
        return content
    except:
        return ""