from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://the-internet.herokuapp.com/")
driver.maximize_window()

driver.find_element_by_xpath("//a[@href='/windows']").click()
driver.find_element_by_link_text("Click Here").click()
childwindow= driver.window_handles[1]

driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element_by_tag_name("h3").text)