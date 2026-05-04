from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
driver = uc.Chrome(version_main=147, options=options)
driver.maximize_window()

driver.get("https://www.pokemon.com/us/")
time.sleep(5)

accept_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Accept')]"))
)
accept_btn.click()

pokedex_link = driver.find_element(By.LINK_TEXT, "Pokédex")
pokedex_link.click()
time.sleep(5)

driver.find_element(By.ID, "searchInput").send_keys("Pikachu")
driver.find_element(By.ID, "search").click()
time.sleep(5)

pikachu_card = driver.find_element(By.XPATH, "//a[contains(@href, 'pikachu')]")
pikachu_card.click()
time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

driver.find_element(By.PARTIAL_LINK_TEXT, "Explore More Cards").click()
time.sleep(5)
driver.quit()

