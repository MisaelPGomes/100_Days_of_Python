from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

#price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
#price_fraction = driver.find_element(By.CLASS_NAME, "a-price-fraction")
#print(f"${price_whole.text}.{price_fraction.text}")

#search_bar =  driver.find_element(By.NAME, "q")
#print(search_bar.tag_name)

python_logo =  driver.find_element(By.CLASS_NAME, "python-logo")
#print(python_logo.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
#print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#print(bug_link.text)


upcoming_event = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')
#//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time
#//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a
event_calendar = {}
keys = range(len(upcoming_event))

#print(upcoming_event[0])
#first_event = upcoming_event[0]
#print(first_event.find_element(By.TAG_NAME, "time").text)
#print(first_event.find_element(By.TAG_NAME, "a").text)

for key in keys:
    event_calendar[key] = {'time': upcoming_event[key].find_element(By.TAG_NAME, "time").text,
                           'name': upcoming_event[key].find_element(By.TAG_NAME, "a").text }


print(event_calendar)

#driver.close()
driver.quit()



