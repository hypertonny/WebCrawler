Web Crawler 🚀
A simple yet powerful web crawler that extracts the main content from any given URL and saves it neatly into both a text file and an Excel spreadsheet — perfect for scraping and analyzing web page data quickly.

✨ Features
Accepts any URL as input

Extracts the main content from the webpage

Saves content as a plain text file (output.txt)

Saves content as an Excel file (output.xlsx)

Optional Selenium version for crawling dynamic websites

🚀 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/hypertonny/WebCrawler.git
cd WebCrawler
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🛠️ Usage
Run the crawler by passing the target URL as an argument:

bash
Copy
Edit
python crawler.py https://example.com
The extracted content will be saved as:

output.txt — Plain text content

output.xlsx — Excel spreadsheet format

🕸️ Crawling Dynamic Websites with Selenium
For websites that load content dynamically (e.g., via JavaScript), use the Selenium-powered crawler:

Ensure Google Chrome is installed.

Download the matching ChromeDriver for your Chrome version and add it to your system PATH.

Install Selenium:

bash
Copy
Edit
pip install selenium
Run the Selenium crawler:

bash
Copy
Edit
python selenium_crawler.py https://example.com
📋 Requirements
Python 3.7 or higher

Packages listed in requirements.txt (requests, beautifulsoup4, openpyxl, etc.)

Optional: selenium for dynamic crawling

📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

📬 Contact
Questions or support? Reach out at:
your.email@example.com

