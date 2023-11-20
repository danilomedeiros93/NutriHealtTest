from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestLogin:
    
    def setup_class(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        
    def test_login(self):
        driver.get('http://localhost:3000/')  
        

        
        time.sleep(10) 
        
        field_login = driver.find_element(By.CSS_SELECTOR, '#container_login > div.row > div.sc-hKgKIp.jITFtB.col-md-6 > div > input:nth-child(3)')
        field_login.send_keys('')
        
        field_password = driver.find_element(By.CSS_SELECTOR, '#container_login > div.row > div.sc-hKgKIp.jITFtB.col-md-6 > div > input:nth-child(4)')
        field_password.send_keys('')
      
        btn_link_sign_in = driver.find_element(By.CSS_SELECTOR,'#container_login > div.row > div.sc-hKgKIp.jITFtB.col-md-6 > div > div.sc-pGaPU.hXoUhX > button') 
        
        btn_link_sign_in.click()
        
       
        
        
        
        time.sleep(10) 
        
    def teardown_class(self):
        driver.close()    