import time
import os
from .searcher import search_duckduckgo
from .fetcher import fetch_raw_paste
from .parser import extract_credentials

def save_leaks(results_dir, paste_url, creds):
    filename = os.path.join(results_dir, paste_url.split("/")[-1] + ".txt")
    with open(filename, "w") as f:
        for cred in creds:
            f.write(cred + "\n")

def run_monitor(company_domain, results_dir="leaks"):
    os.makedirs(results_dir, exist_ok=True)
    print(f"🔍 Searching for leaks for {company_domain}")
    paste_links = search_duckduckgo(company_domain)
    print(f"Found {len(paste_links)} pastes")

    for url in paste_links:
        print(f"\nFetching: {url}")
        content = fetch_raw_paste(url)
        leaks = extract_credentials(content, company_domain)
        if leaks:
            print(f"⚠️  Found {len(leaks)} leaked credentials")
            save_leaks(results_dir, url, leaks)
        else:
            print("✅ No relevant credentials")
        time.sleep(2)