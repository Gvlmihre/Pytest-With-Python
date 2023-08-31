import self as self
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# I need to invoke the chrome driver and Chrome driver will be responsible for invoking the actual browser
# ---Chrome
service_obj = Service("C:\driver\chromedriver.exe")  # I need to give the path of my chrome driver
driver = webdriver.Chrome(service=service_obj)

# ---Firefox
# service_obj = Service('C:\driver\geckodriver.exe')
# driver = webdriver.Firefox(service=service_obj)

# ---Microsoft Edge
# service_obj = Service('C:\driver\msedgedriver.exe')
# driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get('https://www.google.com/')
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com")
driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
print(driver.title)
print(driver.current_url)
