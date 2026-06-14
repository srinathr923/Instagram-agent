import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("user-data-dir=./chrome_profile")

driver = webdriver.Chrome(options=options)

# Put a reel URL here for testing
driver.get("https://www.instagram.com/bmw/reel/DZkn7SHkt2g/")
time.sleep(5)

buttons = driver.find_elements(By.TAG_NAME, "svg")

print(f"Found {len(buttons)} icons")

input("Inspect the page and press Enter...")

driver.quit()