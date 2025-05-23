RERA Odisha Project Scraper
This repository contains a Python-based web scraper for extracting real estate project details from the Odisha RERA portal. The scraper uses Selenium to automate browser interactions, collects key project and promoter information, and saves the results to a CSV file.

Features

Automates data extraction from the official RERA Odisha project list.

Collects details such as RERA Registration Number, Project Name, Promoter Name, Promoter Address, and GST Number.

Saves the extracted data into a structured CSV file for further analysis.

Installation
Clone the repository

bash
git clone <your-repo-url>
cd <repo-directory>
Install dependencies

bash
pip install -r requirements.txt
Dependencies include:

selenium

webdriver-manager

pandas

Usage
Configure Scraper Settings

Edit config.py to adjust scraping parameters such as the number of projects (MAX_PROJECTS) and wait times.

Run the Scraper

bash
python main.py
The scraper will launch a Chrome browser (not headless by default for debugging), navigate the RERA Odisha portal, and extract project data.

Output will be saved as rera_projects.csv in the project directory.

File Structure
File	Description
main.py	Entry point. Initializes the driver, runs the scraper, and saves CSV output.
config.py	Contains configuration variables and XPaths for scraping.
driver_setup.py	Sets up the Selenium Chrome WebDriver.
scraper.py	Core scraping logic and helper functions.
requirements.txt	Python dependencies.
rera_projects.csv	Example output file with scraped project data.
Example Output
The resulting rera_projects.csv will look like:

Rera Regd. No	Project Name	Promoter Name	Promoter Address	GST No
RP/01/2025/01362	Basanti Enclave	M/S. NEELACHAL INFRA DEVELOPERS PVT. LTD	Gurudwara, PO-South Balanda, Via: Talcher Rural INR, Angul-759116...	21AADCN5439J2ZH
...	...	...	...	...
Notes
The scraper is configured to extract up to 6 projects by default. Adjust MAX_PROJECTS in config.py as needed.

Web scraping is subject to changes in website structure. Update XPaths in config.py if the site layout changes.

For headless operation, set headless=True in main.py or modify init_driver() in driver_setup.py.

License
This project is provided for educational and research purposes. Please respect the terms of use of the RERA Odisha portal.
