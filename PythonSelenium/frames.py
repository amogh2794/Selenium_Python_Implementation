from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("kaisa hai lavde")

driver.switch_to.default_content()

print(driver.find_element_by_tag_name("h3").text)