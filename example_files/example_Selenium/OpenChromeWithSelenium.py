import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Chromedriver path
chrome_driver_path = 'C:\\z-BrowserDrivers\\chromedriver.exe'

# Options for Chromedriver
chrome_options = Options()
chrome_options.add_argument('--test-type')
chrome_options.add_argument("--start-maximized")

# Create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://www.google.com/")

time.sleep(10)

# Close browser
driver.close()