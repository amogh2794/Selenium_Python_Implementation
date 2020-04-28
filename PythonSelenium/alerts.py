#handeling java/js alerts

from selenium import webdriver
validateText = "Option3"
validateText2 = "chutya"
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element_by_css_selector("#name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()
driver.find_element_by_css_selector("#name").send_keys("chutya")
driver.find_element_by_id("confirmbtn").click()
alert=driver.switch_to.alert
alertText2=alert.text
assert validateText2 in alertText2
alert.dismiss()