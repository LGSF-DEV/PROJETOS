# entrar no cmd do windowns e dar pip install selenium e pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
#link do site para fazer os testes
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://store.steampowered.com/")

time.sleep(5)
#clickar em iniciar sessão
iniciar = driver.find_element(By.XPATH, '//*[@id="global_action_menu"]/a')
iniciar.click()

time.sleep(2)
#preencher o campo email
email = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[1]/input') 
email.send_keys('COLOQUE O EMAIL AQUI')

time.sleep(2)
#preencher o campo senha
senha = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[2]/input') 
senha.send_keys('COLOQUE A SENHA AQUI')

time.sleep(2)
#clickar no botão iniciar
iniciar = driver.find_element(By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[4]/button')
iniciar.click()

time.sleep(3)

pulldown = driver.find_element(By.ID, 'account_pulldown')
pulldown.click()

time.sleep(2)

detalhesdaconta = driver.find_element(By.XPATH, '//*[@id="account_dropdown"]/div/a[2]')
detalhesdaconta.click()

time.sleep(3)

addphone = driver.find_element(By.XPATH, '//*[@id="main_content"]/div[2]/div[4]/div[2]/div/div/a')
addphone.click()

time.sleep(5)

phonenumber = driver.find_element(By.ID, 'tel_entry')
phonenumber.send_keys('84381234')

time.sleep(5)

driver.execute_script("alert('ERRO,Tente colocar o código do país+ddd+9! Exemplo: +55 98 9 1234-5678')")

time.sleep(5)

alert = driver.switch_to.alert
alert.accept()

time.sleep(5)

driver.close()
