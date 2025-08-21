from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")
driver.get("https://www.python.org/")

# try:
#     continue_btn = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button'))
#     )
#     continue_btn.click()
# except:
#     print("Pop-up çıkmadı veya zaten kapalı.")
#
#
# price_dollar = driver.find_element(By.XPATH, value='//*[@id="_price"]/span')
# price_dollar=price_dollar.text[-6:]
# print(price_dollar)

# element=driver.find_element(By.NAME,value="q")
# print(element.get_attribute("id")) #get attiribute is so important!


times=driver.find_elements(By.CSS_SELECTOR,value=".medium-widget.event-widget.last .menu time")
events=driver.find_elements(By.CSS_SELECTOR,value=".medium-widget.event-widget.last .menu a")
# for time in times:
#     time=time.get_attribute("datetime").split('T')[0]
#
# for event in events:
#     print(event.text)

time_events={}
for i in range(len(times)):
    time_events[i]={"time" :times[i].get_attribute("datetime").split('T')[0],"name" : events[i].text }

print(time_events)


#close method is close the tab

driver.quit()
