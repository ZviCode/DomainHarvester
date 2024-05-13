import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_domains(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        domains = set()

        # Extracting URLs from href attributes of <a> tags
        for tag in soup.find_all('a', href=True):
            href = tag['href']
            parsed_url = urlparse(href)
            domain = parsed_url.netloc
            if domain:
                domains.add(domain)

        # Extracting URLs from src attributes of <script>, <img>, and <link> tags
        for tag in soup.find_all(['script', 'img', 'link'], src=True):
            src = tag['src']
            parsed_url = urlparse(src)
            domain = parsed_url.netloc
            if domain:
                domains.add(domain)

        # Add the main domain if not found in any links
        main_domain = urlparse(url).netloc
        if main_domain not in domains:
            domains.add(main_domain)

        return list(domains)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

