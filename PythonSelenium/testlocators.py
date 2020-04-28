from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.get("https://login.salesforce.com/")
driver.maximize_window()

#driver.find_element_by_css_selector("input[name='name']").send_keys("amogh")
driver.find_element_by_name("name").send_keys("amogh")
driver.find_element_by_name("email").send_keys("amogh2794@gmail.com")
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")

driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text
assert "success" in message  #  for checking if Tc is passed or failed


#driver.find_element_by_css_selector("input#username").send_keys("amogh")
#driver.find_element_by_css_selector(".password").send_keys("asdf")
#driver.find_element_by_css_selector(".password").clear()


#driver.find_element_by_link_text("Forgot Your Password?").click()
#driver.find_element_by_xpath("//a[text()='Cancel']").click()
#print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
#print(driver.find_element_by_xpath("//label[@class='label']").text)


