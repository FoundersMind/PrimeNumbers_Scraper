# config.py

BASE_URL = "https://rera.odisha.gov.in/projects/project-list"
MAX_PROJECTS = 6
PAGE_LOAD_WAIT = 5
DETAILS_LOAD_WAIT = 4
PROMOTER_TAB_WAIT = 3

# Project card and view button
PROJECT_CARD_XPATH = '//*[@id="mainContent"]/form/div[2]/div/div[2]/app-project-card'
VIEW_DETAILS_XPATH_TEMPLATE = '//*[@id="mainContent"]/form/div[2]/div/div[2]/app-project-card/div/div[{i}]/div/div[2]/div[2]/div[2]/a[2]'

# Detail XPaths
RERA_NO_XPATH = '//*[@id="mainContent"]/div/div/app-project-overview/div/div[1]/div/div[2]/div/div[1]/div[4]/div[2]/strong'
PROJECT_NAME_XPATH = '//*[@id="mainContent"]/div/div/app-project-overview/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/strong'

# Promoter details
PROMOTER_NAME_XPATH = '//*[@id="mainContent"]/div/div/app-promoter-details/div[1]/div/div[2]/div/div[1]/div/div[2]/strong'
PROMOTER_ADDRESS_XPATH = '//*[@id="mainContent"]/div/div/app-promoter-details/div[1]/div/div[2]/div/div[6]/div/div[2]/strong'
GST_NO_XPATH = '//label[normalize-space(text())="GST No."]/parent::div/strong'

PROMOTER_TAB_XPATH = '//a[normalize-space(text())="Promoter Details"]'
