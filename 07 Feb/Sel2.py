from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

srev_obl= Service("C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver=webdriver.Chrome(service=srev_obl,options=options)
driver.get("https://www.facebook.com/")

clk=driver.find_element(By.ID,"u_0_0_/h")
clk.click()
