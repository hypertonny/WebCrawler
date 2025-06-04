import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

def crawl_and_save(url, output_file='output.txt', excel_file='output.xlsx'):
    # Add https:// if no protocol is specified
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    try:
        # Initialize the Chrome driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        
        # Load the page
        driver.get(url)
        
        # Wait for dynamic content to load
        time.sleep(5)
        
        # Get the page source after JavaScript execution
        page_source = driver.page_source
        
        # Close the browser
        driver.quit()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')
        
        # Remove unwanted elements
        for element in soup(['script', 'style', 'noscript', 'nav']):
            element.decompose()
        
        # Extract all text content
        content_areas = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'article', 'section', 'div', 'main'])
        
        # Collect all text content
        text_content = []
        for area in content_areas:
            # Get text and remove excessive whitespace
            cleaned_text = ' '.join(area.get_text(separator=' ', strip=True).split())
            if cleaned_text and len(cleaned_text) > 1:  # Only add non-empty content
                text_content.append(cleaned_text)
        
        # Remove duplicates while preserving order
        text_content = list(dict.fromkeys(text_content))
        
        # Join all content with newlines
        full_text = '\n\n'.join(text_content)
        
        # Save to text file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        # Save to Excel
        df = pd.DataFrame(text_content, columns=['Content'])
        df.to_excel(excel_file, index=False)
        
        print(f"Text content saved to '{output_file}'")
        print(f"Excel file saved to '{excel_file}'")
        
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()

# Example usage
url = input("Enter the webpage URL: ")
crawl_and_save(url)