import json
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Load car accounts
with open("data/car_accounts.txt", "r") as f:
    accounts = [line.strip() for line in f if line.strip()]

account = random.choice(accounts)

# Load previously saved reels
saved_file = "data/sent_reels.json"

if os.path.exists(saved_file):
    with open(saved_file, "r") as f:
        saved_reels = json.load(f)
else:
    saved_reels = []

options = Options()
options.add_argument("user-data-dir=./chrome_profile")

driver = webdriver.Chrome(options=options)

driver.get(f"https://www.instagram.com/{account}/reels/")

time.sleep(5)

reels = driver.find_elements(By.TAG_NAME, "a")

new_reel = None

for reel in reels:
    href = reel.get_attribute("href")

    if href and "/reel/" in href:
        if href not in saved_reels:
            new_reel = href
            break

if new_reel:
    print("New reel found:", new_reel)

    saved_reels.append(new_reel)

    with open(saved_file, "w") as f:
        json.dump(saved_reels, f, indent=2)

    driver.get(new_reel)

else:
    print("No new reels found.")

input("Press Enter to close...")

driver.quit()