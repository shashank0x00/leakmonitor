import re

def extract_credentials(text, company_domain):
    regex = rf"[a-zA-Z0-9_.+-]+@{re.escape(company_domain)}:[^\\s]+"
    return re.findall(regex, text)