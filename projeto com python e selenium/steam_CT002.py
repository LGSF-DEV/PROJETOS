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

time.sleep(3)

pulldown = driver.find_element(By.ID, 'account_pulldown')
pulldown.click()

time.sleep(2)

detalhesdaconta = driver.find_element(By.XPATH, '//*[@id="account_dropdown"]/div/a[2]')
detalhesdaconta.click()

time.sleep(3)

addfundos = driver.find_element(By.XPATH, '//*[@id="main_content"]/div[2]/div[2]/div[1]/a[1]')
addfundos.click()

time.sleep(3)

addfundos10 = driver.find_element(By.XPATH, '//*[@id="prices_user"]/div[1]/div/div/a/span')
addfundos10.click()

time.sleep(2)

continuar = driver.find_element(By.XPATH, '//*[@id="submit_payment_info_btn"]/span')
continuar.click()

time.sleep(5)

continuarcompra = driver.find_element(By.ID, 'purchase_button_bottom_text')
continuarcompra.click()

time.sleep(3)

driver.close()
