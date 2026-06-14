from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

options.add_argument(
    "user-data-dir=/Users/srinath/instagram_agent/chrome_profile"
)

driver = webdriver.Chrome(options=options)

driver.get("https://www.instagram.com")

input("Log in manually once, then press Enter...")

driver.quit()