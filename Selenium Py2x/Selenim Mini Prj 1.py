import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

serv_obj= Service("C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://katalon-demo-cura.herokuapp.com/")
url1= driver.current_url

clk=driver.find_element(By.ID,"btn-make-appointment")
driver.maximize_window()
clk.click()
time.sleep(7)
url2=driver.current_url
if url1 == url2:
    print("No URL changed")
else :
    print("URL changed")
driver.find_element(By.NAME,"username").send_keys("John Doe")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
clk=driver.find_element(By.ID,"btn-login").click()
head = driver.find_element(By.CLASS_NAME, "col-sm-12 text-center").text
assert head == "Make Appointment"
time.sleep(10)
driver.quit()