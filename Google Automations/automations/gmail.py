from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\googleautomation\drivers\chromedriver.exe")

driver.set_page_load_timeout(20)
driver.get("https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/")
driver.find_element_by_id("identifierId").send_keys("ENTER_EMAIL_ADDRESS_HERE")
driver.find_element_by_id("identifierNext").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_name("password").send_keys("ENTER_PASSWORD_HERE")
driver.find_element_by_id("passwordNext").send_keys(Keys.ENTER)
time.sleep(4)