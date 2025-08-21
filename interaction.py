from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(chrome_options)
driver.maximize_window()

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_number=driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
# article_number.click()

jim_lovell=driver.find_element(By.LINK_TEXT,value="Jim Lovell")
#jim_lovell.click()

inp_field=driver.find_element(By.NAME,value="search")
inp_field.send_keys("Yusuf Koray Can",Keys.ENTER)


# driver.quit()