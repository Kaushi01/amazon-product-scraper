from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/{query}-Processor-Anti-Glare-Dedicated-Keyboard/dp/B0GWHGS8P5/ref=sr_1_2_sspa?crid=1L270TI0KIX2B&dib=eyJ2IjoiMSJ9.qSHJvRhLngc1zH4myZ1UdivpVuSckkduSDbLivwlFjtESVMofBlal57-IyO5_ja8lvb3L9so4kyvFJ-sKGjV4mFB63FWHcsnM8sa3EALMKOBsqOyektfV-k0gUco9Qef3lm2eszDRXEipKf4I-YXyDXLJasi4IJGrT2gtgsJyidiUfoBf6VwVE5j0d80PTOHrRwvmGEkwO1dib-aYejDv_hceQidrZcPcrKiI77Zz7E.3BTUooQV-qf2F-fSEv4X0Kd3pkRsxlH3buue7xRDCtE&dib_tag=se&keywords=laptop&qid=1794372745&sprefix=laptop%2Caps%2C411&sr=8-2-spons&aref=DdozA4pNQZ&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

elem = driver.find_element(By.CLASS_NAME, "a-size-medium a-color-base a-text-normal")
print(elem.get_attribute("outerHTML"))

time.sleep(6)
driver.close()