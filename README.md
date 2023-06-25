# Webcraping-using-beautiful-soup.
**Web Scraping using Beautiful Soup**

```python
from bs4 import BeautifulSoup
import requests

# Make a request to the website
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract specific elements
data = soup.find('div', class_='class-name').text

# Print the extracted data
print(data)
