from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.python.org")
print(driver.title)

# take screenshot
driver.save_screenshot("test.png")
driver.close()
