# Go to project directory
cd webcrawler

# Create virtual environment (for basic)
python -m venv venv
# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r selenium/requirements.txt

# Run crawler
python basic/selenium-webcrawler.py
