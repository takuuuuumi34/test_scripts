from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# required headless chrome.
# options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=options)

url = "https://www.airbnb.jp/rooms/17113559"
driver.get(url)
print(driver.title)

# class name for price element.
elm = driver.find_element_by_class_name("_10cqp947")
print(elm.text)
driver.close()

