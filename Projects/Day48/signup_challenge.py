from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME, "fName")
name.send_keys("Misael")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Peixoto Gomes")

email = driver.find_element(By.NAME, "email")
email.send_keys("misapeixoto@gmail.com")

submit_button = driver.find_element(By.TAG_NAME, "button")
submit_button.click()

