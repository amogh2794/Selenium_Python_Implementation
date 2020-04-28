#implisit wait is dynamic i.e if object is visible it will resume the execution if object doesnt show then it will wait for no.of seconds


from selenium import webdriver
import time
itemsadded = []
items = []
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("ber")
time.sleep(4)
nop = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert nop == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for btn in buttons:
    itemsadded.append(btn.find_element_by_xpath("parent::div/parent::div/h4").text)
    btn.click()

print(itemsadded)
driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button[text()='PROCEED TO CHECKOUT']").click()

veggies = driver.find_elements_by_css_selector("p.product-name")

for veg in veggies:
    items.append(veg.text)

print(items)
#assert itemsadded == items
originalAmt = driver.find_element_by_css_selector(".discountAmt").text
print(originalAmt)
driver.find_element_by_xpath("//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector(".promoInfo").text)
discountAmt = driver.find_element_by_css_selector(".discountAmt").text
print(discountAmt)
assert float(discountAmt) < float(originalAmt)
totalamt = driver.find_element_by_css_selector(".totAmt").text
amts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amt in amts:
    sum = sum + int(amt.text)

print(sum)

assert int(totalamt) == sum