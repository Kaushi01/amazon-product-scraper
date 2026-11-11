# Amazon Product Scraper

A Python-based web scraping project that demonstrates browser automation and HTML data extraction using Selenium and BeautifulSoup.

## Project Overview

This project automates the process of collecting product information from e-commerce search result pages.

It uses Selenium to navigate search pages and extract HTML elements, while BeautifulSoup parses the saved HTML documents to retrieve product information.

## Technologies Used

- Python
- Selenium
- BeautifulSoup
- HTML Parsing
- File Handling

## Project Structure

```text
amazon-product-scraper/
│
├── data/
├── project.py
├── collect.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Workflow

1. Define a product search query.
2. Use Selenium WebDriver to navigate search result pages.
3. Locate relevant HTML elements.
4. Extract and save HTML content.
5. Use BeautifulSoup to parse the saved HTML.
6. Extract product information from the HTML structure.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/amazon-product-scraper.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Execution

Run the scraping script:

```bash
python project.py
```

Run the HTML parsing script:

```bash
python collect.py
```

## Learning Outcomes

- Browser automation using Selenium
- Locating web elements
- HTML extraction and parsing
- Working with BeautifulSoup
- File handling and data collection
- Automating repetitive web tasks

## Disclaimer

This project is intended for educational purposes. Always respect the target website's terms of service, robots.txt policies, and applicable data usage restrictions. Do not bypass access restrictions or anti-bot protections.
