# Web Crawler

A simple web crawler that takes a URL as input and extracts the page content, saving it into both a text file and an Excel spreadsheet.

## Features

- Accepts a URL as input
- Extracts the main content of the web page
- Saves the content into a `.txt` file
- Saves the content into an `.xlsx` Excel file

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/webcrawler.git
   cd webcrawler
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Run the crawler with the target URL as an argument:

bash
Copy
Edit
python crawler.py https://example.com
The extracted content will be saved as:

output.txt — containing the plain text content

output.xlsx — containing the content in Excel format

Requirements
Python 3.7 or higher

Packages listed in requirements.txt (e.g., requests, openpyxl, beautifulsoup4)

Optional Selenium Version
A Selenium-based version is also included for crawling dynamic websites. To use it:

Make sure you have Google Chrome installed.

Download the matching ChromeDriver and place it in your PATH.

Install Selenium:

bash
Copy
Edit
pip install selenium
Run the Selenium crawler script:

bash
Copy
Edit
python selenium_crawler.py https://example.com
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or support, contact [your.email@example.com].