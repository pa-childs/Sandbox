import time
from selenium import webdriver

# Chromedriver path
ie_driver_path = 'C:\z-BrowserDrivers\IEDriverServer.exe'

# Create a new IE session
driver = webdriver.Ie(ie_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com/")

time.sleep(10)

# Close browser
driver.close()