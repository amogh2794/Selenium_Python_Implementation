from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https:\\www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_name("name").send_keys("hello")



print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shop = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",shop)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")