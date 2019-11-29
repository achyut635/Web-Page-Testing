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

        urls = ['https://www.google.com']
        for url in urls:
         driver.get(url)
         x = driver.find_element_by_class_name("gb_g")
         webdriver.ActionChains(driver).move_to_element(x).click(x).perform()
         y = driver.current_url
         assert "https://mail.google.com/mail/u/0/" in y

    
        
