import time
import pandas as pd
from selenium.webdriver.common.by import By
from config import *

def scrape_projects(driver):
    data = []

    for i in range(1, MAX_PROJECTS + 1):  # 1-based indexing
        try:
            driver.get(BASE_URL)
            time.sleep(PAGE_LOAD_WAIT)

            view_xpath = VIEW_DETAILS_XPATH_TEMPLATE.format(i=i)
            view_button = driver.find_element(By.XPATH, view_xpath)

            driver.execute_script("arguments[0].scrollIntoView(true);", view_button)
            driver.execute_script("arguments[0].click();", view_button)
            time.sleep(DETAILS_LOAD_WAIT)

            details = extract_project_details(driver)
            promoter_details = extract_promoter_details(driver)
            details.update(promoter_details)
            data.append(details)

        except Exception as e:
            print(f"❌ Error processing project {i}: {e}")

    return pd.DataFrame(data)


def extract_project_details(driver):
    return {
        "Rera Regd. No": get_element_text(driver, RERA_NO_XPATH),
        "Project Name": get_element_text(driver, PROJECT_NAME_XPATH),
    }


def extract_promoter_details(driver):
    try:
        promoter_tab = driver.find_element(By.XPATH, PROMOTER_TAB_XPATH)
        driver.execute_script("arguments[0].scrollIntoView(true);", promoter_tab)
        driver.execute_script("arguments[0].click();", promoter_tab)
        time.sleep(PROMOTER_TAB_WAIT)
    except Exception as e:
        print(f"❌ Could not click Promoter Details tab: {e}")
        return {
            "Promoter Name": "N/A",
            "Promoter Address": "N/A",
            "GST No": "N/A",
        }

    return {
        "Promoter Name": get_element_text(driver, PROMOTER_NAME_XPATH),
        "Promoter Address": get_element_text(driver, PROMOTER_ADDRESS_XPATH),
        "GST No": get_element_text(driver, GST_NO_XPATH),
    }


def get_element_text(driver, xpath):
    try:
        el = driver.find_element(By.XPATH, xpath)
        return el.text.strip()
    except Exception:
        return "N/A"
