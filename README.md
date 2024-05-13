# DomainHarvester

## Overview
DomainHarvester is a Python tool designed to extract unique domains from specified URLs. It scans through the HTML content of each URL, collects domains from various tag attributes, and outputs a list of unique domain names.

## Features
- Fetch HTML content from URLs.
- Extract domains from `<a>`, `<script>`, `<img>`, and `<link>` tags.
- Support for handling HTTP errors gracefully.
- Output a unique set of domains for a list of given URLs.

## Requirements
- Python 3.7
- pip install -r requirements.txt


## Usage
To use DomainHarvester, you need to provide a list of URLs. The tool will process each URL and print out a list of unique domains extracted from these URLs.

### Example
```python
from domain_harvester import extract_domains

# List of URLs to process
urls = ['https://www.example.com/', 'https://www.anotherdomain.com/']

# Extract domains
unique_domains = []
for url in urls:
    domains = extract_domains(url)
    if domains:
        unique_domains.extend([domain for domain in domains if domain not in unique_domains])

print("Unique domains extracted:", unique_domains)
```

## Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your suggested changes.

