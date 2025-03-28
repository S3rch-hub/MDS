

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Sergio/Desktop/Ciberseguridad/3%C2%BA%20Ciberseguridad/Metodolog%C3%ADas%20de%20desarrollo%20seguro/Whack-a-Mole/index.html")




while int(driver.find_element(By.ID,"score").text) <= 10000:
    try:
        hoyos = driver.find_element(By.CLASS_NAME,"mole")
        hoyos.click()

    except:
        pass
input()
driver.close()
driver.quit()