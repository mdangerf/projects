from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\googleautomation\drivers\chromedriver.exe")

driver.set_page_load_timeout(20)
driver.get("https://accounts.google.com/signin/v2/identifier?service=cl&passive=1209600&osid=1&continue=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Frender%3Ftab%3Dwc&followup=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Frender%3Ftab%3Dwc&scc=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_id("identifierId").send_keys("ENTER_EMAIL ADDRESS_HERE")
driver.find_element_by_id("identifierNext").send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_name("password").send_keys("ENTER_PASSWORD_HERE")
driver.find_element_by_id("passwordNext").send_keys(Keys.ENTER)
time.sleep(4)
