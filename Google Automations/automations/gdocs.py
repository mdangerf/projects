from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\googleautomation\drivers\chromedriver.exe")

driver.set_page_load_timeout(20)
driver.get("https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdocs.google.com%2Fdocument%2F%3Fusp%3Ddocs_alc&followup=https%3A%2F%2Fdocs.google.com%2Fdocument%2F%3Fusp%3Ddocs_alc&ltmpl=docs&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_id("identifierId").send_keys("ENTER_EMAIL_ADDRESS_HERE")
driver.find_element_by_id("identifierNext").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_name("password").send_keys("ENTER_PASSWORD_HERE")
driver.find_element_by_id("passwordNext").send_keys(Keys.ENTER)
time.sleep(4)
