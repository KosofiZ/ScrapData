
""" import requests
from bs4 import BeautifulSoup
import pdfkit
import os

# Path to the file containing the URLs
url = "https://developer.salesforce.com/docs/marketing/personalization/guide/get-started.html"

# Create a directory to save PDF files
output_directory = "pdf_file"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Set options for pdfkit
options = {
    'quiet': ''
}


response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# Extract relevant data from the webpage (customize as per your requirements)
title = soup.find('h1')
body = soup.find_all('p')
#subtitle = soup.find_all('span', class_="title")




for paragraph in body:
    print(paragraph.get_text())

# Generate PDF filename from the URL
filename = url.split("/")[-1] + ".pdf"
filepath = os.path.join(output_directory, filename)

# Convert webpage content to PDF
pdfkit.from_string(f"<h1>{title}</h1><p>{body}</p>", filepath, options=options)

#print(f"PDF saved: {filepath}")
 """



import requests
from bs4 import BeautifulSoup
import pdfkit
import os

# URL of the webpage
url = "https://developer.salesforce.com/docs/marketing/personalization/guide/get-started.html"

# Create a directory to save PDF files
output_directory = "pdf_file"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Set options for pdfkit
options = {
    'quiet': ''
}

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract relevant data from the webpage
title = soup.find('h1').get_text()  # Get text content of the <h1> tag
paragraphs = soup.find_all('p')  # Find all <p> tags
body_text = '<br>'.join(paragraph.get_text() for paragraph in paragraphs)  # Concatenate text from all <p> tags

# Generate PDF filename from the URL
filename = url.split("/")[-1] + ".pdf"
filepath = os.path.join(output_directory, filename)

# Convert webpage content to PDF
html_content = f"<h1>{title}</h1><p>{body_text}</p>"
pdfkit.from_string(html_content, filepath, options=options)

print(f"PDF saved: {filepath}")
