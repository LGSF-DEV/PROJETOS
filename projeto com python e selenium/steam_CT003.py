# entrar no cmd do windowns e dar pip install selenium e pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
#link do site para fazer os testes
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

time.sleep(5)

pulldown = driver.find_element(By.ID, 'account_pulldown')
pulldown.click()

time.sleep(2)

detalhesdaconta = driver.find_element(By.XPATH, '//*[@id="account_dropdown"]/div/a[2]')
detalhesdaconta.click()

time.sleep(5)

addcard = driver.find_element(By.XPATH, '//*[@id="main_content"]/div[2]/div[2]/div[1]/a[2]')
addcard.click()

time.sleep(3)

cardnumber = driver.find_element(By.ID, 'card_number') 
cardnumber.send_keys('1234 1234 1234 1234 1234')

time.sleep(2)

month = driver.find_element(By.ID, 'expiration_month_trigger')
month.click()

time.sleep(2)

day = driver.find_element(By.XPATH, '//*[@id="01"]')
day.click()

time.sleep(2)

year = driver.find_element(By.ID, 'expiration_year_trigger')
year.click()

time.sleep(2)

yearyear = driver.find_element(By.XPATH, '//*[@id="2023"]')
yearyear.click()

time.sleep(2)

securitycode = driver.find_element(By.ID, 'security_code') 
securitycode.send_keys('123')

time.sleep(2)

firstname = driver.find_element(By.ID, 'first_name') 
firstname.send_keys('LUCAS')

time.sleep(2)

lastname = driver.find_element(By.ID, 'last_name') 
lastname.send_keys('GABRIEL')

time.sleep(2)

address = driver.find_element(By.ID, 'billing_address') 
address.send_keys('Av Neiva Moreira')

time.sleep(2)

addresstwo = driver.find_element(By.ID, 'billing_address_two') 
addresstwo.send_keys('Varandas Grand Park')

time.sleep(2)

city = driver.find_element(By.ID, 'billing_city') 
city.send_keys('São Luís')

time.sleep(2)

postalcode = driver.find_element(By.ID, 'billing_postal_code') 
postalcode.send_keys('65075-441')

time.sleep(2)

phone = driver.find_element(By.ID, 'billing_phone') 
phone.send_keys('98 4009-7073')

time.sleep(2)

continuar = driver.find_element(By.XPATH, '//*[@id="submit_payment_info_btn"]/span')
continuar.click()

time.sleep(5)

driver.close()
