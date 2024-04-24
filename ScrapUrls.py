""" import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

URL = "https://developer.salesforce.com/sitemap-1.xml"

# Path where you want to save the HTML content
file_name = 'ziad.txt'

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
time.sleep(5)

#print(webpage.status_code)
soup = BeautifulSoup(webpage.content, 'html.parser')
soup_str = soup.prettify()

# Writing the HTML content to a file
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(soup_str) """


import requests
import xml.etree.ElementTree as ET
import pandas as pd
import time

URL = "https://developer.salesforce.com/sitemap-1.xml"

# Path where you want to save the URLs
file_name = 'urlsmarketing.txt'

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})

webpage = requests.get(URL, headers=HEADERS)
time.sleep(5)

# Parse XML content
tree = ET.fromstring(webpage.content)

# Extract URLs from the XML
#urls = [url.text.strip() for url in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]



# Extract URLs from the XML that contain "marketing/"
urls = [url.text.strip() for url in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc") if 'marketing/' in url.text]

# Writing the URLs to a file
with open(file_name, 'w', encoding='utf-8') as file:
    for url in urls:
        file.write(url + '\n')
