from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

service = Service("C:\\Users\\Pranathi\\Downloads\\edgedriver_win64\\msedgedriver.exe")

driver = webdriver.Edge(service=service)
driver.get("https://www.facebook.com")
time.sleep(20)

driver.quit()
