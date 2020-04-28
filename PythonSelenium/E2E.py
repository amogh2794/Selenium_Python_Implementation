from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https:\\www.rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element_by_css_selector("a[href*='shop']").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

for product in products:
    prodName = product.find_element_by_xpath("div/h4/a").text
    driver.execute_script("window.scrollTo(0,200);")
    if prodName == "Blackberry":
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()

driver.find_element_by_css_selector("button[class*='btn-success']").click()

#driver.find_element_by_css_selector("input[id*='checkbox2']").click()

driver.find_element_by_css_selector("input[id*='country'").send_keys("India")
#wait = WebDriverWait(driver, 10)
#wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT,"India"))
#driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//a[text()='India']").click()
driver.find_element_by_css_selector("input[class*='btn-lg']").click()
successText = driver.find_element_by_class_name("alert-success").text
assert "Success! Thank you" in successText
driver.get_screenshot_as_file("screen.png")