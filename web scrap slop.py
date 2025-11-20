import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "https://example.com"
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract data
# Find all paragraphs
paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p.text)

# Find elements by class
items = soup.find_all('div', class_='item-name')
for item in items:
    print(item.text)

# Find elements by id
header = soup.find(id='main-header')
print(header.text)
