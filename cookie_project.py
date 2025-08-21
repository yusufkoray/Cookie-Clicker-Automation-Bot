from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.maximize_window()

driver.get("https://ozh.github.io/cookieclicker/")

cookie = driver.find_element(By.ID, value="bigCookie")

driver.implicitly_wait(10)  # We have to wait untill the page is fully loaded. Otherwise we can not get any data


def get_data():
    #print(driver.find_element(By.CSS_SELECTOR, value="#cookies.title").text)
    cookies_number = driver.find_element(By.CSS_SELECTOR, value="#cookies.title").text.split(' ')[0].replace(',','')
    cookies_number = float(cookies_number.split('\n')[0])
    print(cookies_number)
    product_titles = driver.find_elements(By.CSS_SELECTOR, value="#sectionRight #store #products .title:not(.owned)")
    #.title:not(.owned) means that, take "title", don't take title owned.
    #When the code runs, if we don't write this code, after 2 or 3 seconds code will take number.
    #Because of this, program doesn't work properly.
    products_prices = driver.find_elements(By.CSS_SELECTOR, value="#sectionRight .price")
    products_data = {}

    for i in range(len(products_prices)):
        products_data[product_titles[i].text.split('\n')[0]] = float(products_prices[i].text.replace(',', ''))
    print(products_data)
    return products_data, cookies_number


def buy_new_skill(biggest_title):
    enabled_items = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
    for e_item in enabled_items:
        title = e_item.find_element(By.CSS_SELECTOR, ".title").text
        if title == biggest_title:
            e_item.click()
            break


time_out_start = time.time()
timeout = 300
check_time = 20

while True:
    if time.time() - time_out_start >= check_time:
        time_out_start = time.time()
        products_data_ = get_data()
        purchasable_cookies = {}
        for key, value in products_data_[0].items():
            if products_data_[1] >= value:
                purchasable_cookies[key] = value

        max_value = max(purchasable_cookies.values())
        max_key = next(key for key, value in purchasable_cookies.items() if value == max_value)
        print(max_key)
        buy_new_skill(max_key)

    cookie.click()


# driver.quit()
