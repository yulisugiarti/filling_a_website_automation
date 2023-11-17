

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

driver.get("https://secure-retreat-92358.herokuapp.com/")

#let say my first name and last name is the same
elements = ["fName", "lName"]
for x in elements:
    name = driver.find_element(By.NAME, value=x)
    name.send_keys("yui")

mailing = driver.find_element(By.NAME, value="email").send_keys("yuli@gmail")

Sign_Up = driver.find_element(By.CLASS_NAME, value="btn")
Sign_Up.click()
