import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import ctypes

class TestClass:
    def test_url(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(4)
        user32 = ctypes.WinDLL('user32')
        SW_MAXIMISE = 3
        hWnd = user32.GetForegroundWindow()
        user32.ShowWindow(hWnd, SW_MAXIMISE)

        urls = ['https://www.linkedin.com']
        for url in urls:
         driver.get(url)
         #element = driver.find_element_by_class_name("sign-in-form")
         inputElement = driver.find_element_by_name("session_key")
         inputElement.send_keys('xxxxxxxs')
         inputElement = driver.find_element_by_name("session_password")
         inputElement.send_keys('xxxxxxx')
         inputElement.send_keys(Keys.ENTER)
         y = driver.current_url
         assert "https://www.linkedin.com/feed/?trk=guest_homepage-basic_sign-in-submit" in y

    
        
