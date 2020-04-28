from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https:\\www.rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https:\\www.rahulshettyacademy.com/AutomationPractice/")
driver.back()
driver.refresh()


driver.close() # there is another method deirve.quit() which closes all  browser windows