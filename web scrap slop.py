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


''''

def weather_by_location(location="Bhubaneswar"):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Get free at openweathermap.org
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location},IN&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print(f"Weather in {data['name']}, {data['sys']['country']}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")

weather_by_location("Bhubaneswar")
''''

