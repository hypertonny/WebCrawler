import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def crawl_and_save(url, output_file='output.txt'):
    try:
        # Ensure the URL has a scheme
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url

        response = requests.get(url, timeout=10, verify=False)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Remove script and style elements
    for script_or_style in soup(['script', 'style', 'noscript']):
        script_or_style.decompose()

    # Get clean text
    text = soup.get_text(separator='\n', strip=True)

    # Save to text file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"Text content saved to '{output_file}'")

# Example usage:
url = input("Enter the webpage URL: ")
crawl_and_save(url)
