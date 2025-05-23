# RERA Odisha Project Scraper

This repository provides a Python web scraper to extract real estate project details from the Odisha RERA portal using Selenium. The scraper automates browser actions, collects project and promoter data, and saves the results in a CSV file.

---

## Features

- Automates data extraction from the official RERA Odisha project list.
- Captures details: RERA Registration Number, Project Name, Promoter Name, Promoter Address, and GST Number.
- Outputs structured data to `rera_projects.csv`.

---

## Installation

1. **Clone the repository**
git clone <your-repo-url>
cd <repo-directory>

2. **Install dependencies**
pip install -r requirements.txt
_Dependencies:_
- selenium
- webdriver-manager
- pandas

---

## Usage

1. **Configure Scraper Settings**
- Edit `config.py` to adjust scraping parameters such as `MAX_PROJECTS` and wait times[1].

2. **Run the Scraper**

- The scraper will launch Chrome (not headless by default), navigate the RERA Odisha portal, and extract project data[3].
- Output is saved as `rera_projects.csv` in the project directory[3].

---

## File Structure

| File                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `main.py`           | Entry point. Initializes the driver, runs the scraper, and saves CSV output[3]. |
| `config.py`         | Scraper configuration and XPaths[1].                                        |
| `driver_setup.py`   | Selenium Chrome WebDriver setup[2].                                         |
| `scraper.py`        | Core scraping logic and helper functions[6].                                |
| `requirements.txt`  | Python dependencies[4].                                                     |
| `rera_projects.csv` | Example output file with scraped project data[5].                           |

---

## Example Output

The resulting `rera_projects.csv` will look like:

| Rera Regd. No     | Project Name          | Promoter Name                           | Promoter Address                                                    | GST No         |
|-------------------|----------------------|-----------------------------------------|---------------------------------------------------------------------|---------------|
| RP/01/2025/01362  | Basanti Enclave      | M/S. NEELACHAL INFRA DEVELOPERS PVT. LTD| Gurudwara, PO-South Balanda, Via: Talcher Rural INR, Angul-759116...| 21AADCN5439J2ZH|
| RP/19/2025/01361  | UDYAYEEN             | SHYAMCHAND BUILDERS PRIVATE LIMITED     | MIG-II 21/2 Ground Floor, Chandrasekharpur, Bhubaneswar, ...        | 21ABCCS4755J1ZB|
| ...               | ...                  | ...                                     | ...                                                                 | ...           |

---

## Notes

- The scraper is configured to extract up to 6 projects by default. Adjust `MAX_PROJECTS` in `config.py` as needed[1].
- Website structure changes may require updates to XPaths in `config.py`[1].
- For headless operation, set `headless=True` in `main.py` or modify `init_driver()` in `driver_setup.py`[2][3].

---

## License

This project is for educational and research use. Please comply with the terms of use of the RERA Odisha portal.

---

**Contact:**  
For issues or suggestions, open an issue or submit a pull request.
