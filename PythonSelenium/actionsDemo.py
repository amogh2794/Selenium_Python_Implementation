from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.familysearch.org/en/")
driver.maximize_window()
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("")).perform()
action.move_to_element(driver.find_element_by_link_text("Genealogies")).click().perform()