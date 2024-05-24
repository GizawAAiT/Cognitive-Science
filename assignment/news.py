import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the webpage using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all paragraphs on the webpage
            paragraphs = soup.find_all('p')
            # Concatenate the text content of all paragraphs into a single string
            content = ' '.join([p.get_text() for p in paragraphs])
            return content
        else:
            print("Failed to retrieve content. Status code:", response.status_code)
            return None
    
    except Exception as e:
        print("An error occurred:", str(e))
        return None

