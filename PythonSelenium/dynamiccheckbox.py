# for clicking all checkboxes on the page

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
for i in checkboxes:
    if i.get_attribute("value") =="option2":
        i.click()
        assert (i.is_selected())

radiobtns= driver.find_elements_by_name("radioButton")
radiobtns[2].click()