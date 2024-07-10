import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
def test_pustak_bookname():
    driver = webdriver.Chrome()
    driver.get("https://mypustak.com/")
    driver.implicitly_wait(10)
    element = driver.find_element(By.XPATH, "//*[text()='Objecive Mathematic Volumes 1 For Jee Main & Advan...']")

    book_title = element.get_attribute('h1').text
    print(book_title)
    #assert 'Objecive Mathematic VOLUMES 1' in book_title