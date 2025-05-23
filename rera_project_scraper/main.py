from driver_setup import init_driver
from scraper import scrape_projects
import pandas as pd

# ✅ Initialize driver with full-screen (not headless for visual debugging)
driver = init_driver(headless=False)
driver.maximize_window()

# ✅ Scrape data
data = scrape_projects(driver)
driver.quit()

# ✅ Convert list of dicts to DataFrame
df = pd.DataFrame(data)

# ✅ Save to CSV
df.to_csv("rera_projects.csv", index=False)

print("✅ Scraping complete. Data saved to rera_projects.csv")
