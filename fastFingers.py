
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 
driver.get("file:///C:/Users/Sergio/Desktop/Ciberseguridad/3º%20Ciberseguridad/Metodologías%20de%20desarrollo%20seguro/10fastfingers/index.html")

caja = driver.find_element(By.ID,"textInput")
for i in range(1,21):
    word = driver.find_element(By.ID,f"word_{i}")
    caja.send_keys(word.text + " ")

input()
driver.close()
driver.quit()