import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("mumbai")
time.sleep(2)
fcities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(fcities))
for fc in fcities:
    if fc.text == "Mumbai, India":
        fc.click()
        break

driver.find_element_by_xpath("//input[text()='Dublin, Ireland']").click()

