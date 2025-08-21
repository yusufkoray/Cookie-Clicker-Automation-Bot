from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(chrome_options)
driver.maximize_window()

driver.get("https://secure-retreat-92358.herokuapp.com/")

name=driver.find_element(By.NAME,value="fName")
name.send_keys("Yusuf Koray")
last_name=driver.find_element(By.NAME,value="lName")
last_name.send_keys("Can")
email=driver.find_element(By.NAME,value="email")
email.send_keys("ykcykcykcykc@gmail.com")
sign_up_btn = driver.find_element(By.CLASS_NAME,value="btn.btn-lg.btn-primary.btn-block")
sign_up_btn.click()
# driver.quit()