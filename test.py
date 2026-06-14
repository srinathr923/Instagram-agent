from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.instagram.com")

input("Instagram opened. Press Enter to close...")

driver.quit()
