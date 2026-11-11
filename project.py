from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file=0
for i in range(1, 20):
    url = f"https://www.amazon.in/s?k={query}&page={i}&xpid=hNIccph2ucjql&crid=1L270TI0KIX2B&qid=1794372745&sprefix=laptop%2Caps%2C411&ref=sr_pg_2"
    driver.get(url)

    elems = driver.find_elements(By.CLASS_NAME, "a-size-medium")
    print(f"{len(elems)} elements found")
    print(elems)
    for elem in elems:
      d= elem.get_attribute("outerHTML")
      with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
         f.write(d) 
         file+=1
    #print(elem.text)

    time.sleep(6)
driver.close()