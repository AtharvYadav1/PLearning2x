from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url='https://www.google.com'
chrome_opt = Options()
chrome_opt.add_experimental_option("detach",True)
#serv_obj=Service("C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_opt)

driver.get(url)
driver.maximize_window()

