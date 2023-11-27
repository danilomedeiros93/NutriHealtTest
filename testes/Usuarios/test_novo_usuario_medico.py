from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TestCadastro:
    
    def setup_class(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        
    def test_cadastro_medico(self):
        driver.get('http://localhost:3000/')  

        
        time.sleep(10) 
        
        field_login = driver.find_element(By.CSS_SELECTOR, '#container_login > div.row > div.sc-hKgKIp.jITFtB.col-md-6 > div > input:nth-child(3)')
        field_login.send_keys('admin')
        
        field_password = driver.find_element(By.CSS_SELECTOR, '#container_login > div.row > div.sc-hKgKIp.jITFtB.col-md-6 > div > input:nth-child(4)')
        field_password.send_keys('admin')
        
        btn_link_sign_in = driver.find_element(By.CSS_SELECTOR,'#container_login > div.row > div.sc-hKgKIp.jITFtB.col-md-6 > div > div.sc-pGaPU.hXoUhX > button') 
        btn_link_sign_in.click()

        time.sleep(3)
        
        btn_link_sign_in = driver.find_element(By.CSS_SELECTOR,'#container_principal > div.sc-fodVRF.iXzTJX.justify-content-center.row >div > div.sc-hHftZz.gCxOuQ > a > div') 
        btn_link_sign_in.click()
        
        time.sleep(3)
        
        btn_link_sign_in = driver.find_element(By.CSS_SELECTOR,'#container_principal > div:nth-child(2) > div.col > div') 
        btn_link_sign_in.click()
        
        driver.find_element(By.NAME,'username').send_keys('Danilo Medeiros')
        driver.find_element(By.NAME,'cpf').send_keys('22222222222')
        driver.find_element(By.NAME,'number').send_keys('83982103979')
        driver.find_element(By.NAME,'email').send_keys('danilomedeiros@gmail.com')
        driver.find_element(By.NAME,'addressCity').send_keys('Patos')
        driver.find_element(By.NAME,'addressUF').send_keys('PB')
        driver.find_element(By.NAME,'addressNeighborhood').send_keys('Belo Horizonte')
        driver.find_element(By.NAME,'addressStreet').send_keys('Rua Jose Eduardo')
        
        btn_link_sign_in = driver.find_element(By.CSS_SELECTOR,'#root > div > div.sc-fFubCH.bWyetZ.row > div:nth-child(2) > div.sc-ezrdqu.bxgSek > button') 
        btn_link_sign_in.click()  
        
             
            
        
        time.sleep(10) 
        
    def teardown_class(self):
        driver.close()    