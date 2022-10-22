from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")


start = time.time()

end= 0
click = True
scr = "1,081"
print(float(scr.replace(",", "")))
while click:
    if end < start + 5:
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()
        end= time.time()
    else:
        score_string = driver.find_element(By.ID, "money").text
        score = score_string.replace(",", "")
        print(score)
        #cursor = driver.find_element(By.ID, "buyGrandma")
        #cursor.click()
        if float(score) >= 100 and float(score)<500:
            grandma = driver.find_element(By.ID, "buyGrandma")
            grandma.click()
        elif float(score) >= 500:
            factory = driver.find_element(By.ID, "buyFactory")
            factory.click()
           # elif score >111 and score <= 500:
           #     factory = driver.find_element(By.ID, "buyFactory")
           #     factory.click()
        start = time.time()
