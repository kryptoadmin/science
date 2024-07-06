"""
Real world example: Multi threading I/O bound tasks
Scenario: Web scraping
Web scraping often involves making multiple fetch request to web pages
These tasks are I/O bound as they will be mostly waiting for the responses from server
"""

import threading
import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.w3schools.com/python/python_operators.asp",
    "https://www.w3schools.com/python/python_conditions.asp",
    "https://www.w3schools.com/python/python_iterators.asp"
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Total length of the content is {len(soup.text)} characters")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("**** End of execution ****")