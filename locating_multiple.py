from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
for i in range(1, 20):
    url = f"https://www.amazon.in/s?k={query}&page={i}&xpid=hNIccph2ucjql&crid=1L270TI0KIX2B&qid=1794372745&sprefix=laptop%2Caps%2C411&ref=sr_pg_2"
    driver.get(url)

    elems = driver.find_elements(By.CLASS_NAME, "a-size-medium")
    print(f"{len(elems)} elements found")
    print(elems)
    for elem in elems:
        print(elem.text)
    #print(elem.get_attribute("outerHTML"))
    #print(elem.text)

    time.sleep(6)
    driver.close()