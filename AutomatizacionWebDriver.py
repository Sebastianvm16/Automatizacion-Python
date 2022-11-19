from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Precio del Bitcoin con Web Scraping (Python y Selenium)

#PATH = 'C:/chrome_webdriver/chromedriver.exe'

#driver = webdriver.Chrome(PATH)
driver = webdriver.Firefox(executable_path="geckodriver.exe")

driver.get("https://www.horamundial.com")



España = driver.find_element(By.XPATH,'//*[@id="Reloj4"]')
Usa = driver.find_element(By.XPATH,'//*[@id="Reloj5"]')
Tokio = driver.find_element(By.XPATH,'//*[@id="Reloj3"]')


print('Esta es la hora en españa: '+ España.text)

print('Esta es la hora en Estados unido: '+ Usa.text)

print('Esta es la hora en Tokio: '+ Tokio.text)
         
driver.quit()