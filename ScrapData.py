""" import os
from bs4 import BeautifulSoup
import requests
import pdfkit

# Path to the file containing the URLs
url_file = 'urlsmarketing.txt'

# Create a directory to save PDF files
output_directory = "pdf_files"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Set options for pdfkit
options = {
    'quiet': '',
    'print-media-type': None 
}

# Read URLs from the file
with open(url_file, 'r') as file:
    urls = file.readlines()
    urls = [url.strip() for url in urls]

# Loop through each URL, scrape data, and save as PDF
for url in urls:
    # Fetch HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract relevant data from the webpage (customize as per your requirements)
    big_title = soup.find("title").string
    header = soup.find("span", class_="title")
    p = soup.find("p")

    # Generate PDF filename from the URL
    filename = url.split("/")[-1] + ".pdf"
    filepath = os.path.join(output_directory, filename)


    pdfkit.from_string(f"<h1>{big_title}</h1>{p}", filepath, options=options)

    print(f"PDF saved: {filepath}")
 """


import requests
from bs4 import BeautifulSoup
import pdfkit
import os

# Path to the file containing the URLs
url_file = 'urlsmarketing.txt'

# Create a directory to save PDF files
output_directory = "pdf_files"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Set options for pdfkit
options = {
    'quiet': ''
}

# Read URLs from the file
with open(url_file, 'r') as file:
    urls = file.readlines()
    urls = [url.strip() for url in urls]

# Loop through each URL, scrape data, and save as PDF
for url in urls:
    # Fetch HTML content
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract relevant data from the webpage (customize as per your requirements)
    title = soup.title.string
    body = soup.find('body').get_text()

    # Generate PDF filename from the URL
    filename = url.split("/")[-1] + ".pdf"
    filepath = os.path.join(output_directory, filename)

    # Convert webpage content to PDF
    pdfkit.from_url(url, filepath, options=options)

    print(f"PDF saved: {filepath}")
