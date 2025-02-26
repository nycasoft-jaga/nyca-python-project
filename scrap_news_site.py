import requests
from bs4 import BeautifulSoup

# The URL we want to scrape
url = "https://www.bbc.com/news"

# Send a request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    # Save the parsed HTML to a file
    with open('output.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    # Find the top headline (BBC uses specific classes, subject to change)
    headline = soup.find("h2")  # This targets the first <h2> tag, often a headline
    
    # Print the result
    if headline:
        print("Top Headline:", headline.text.strip())
    else:
        print("Couldn’t find a headline!")
else:
    print("Failed to load the page. Status code:", response.status_code)