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
# AÇÃO NÃO AUTOMÁTICA: ir no campo com o nome do usuário e cliclar em amigos, DEPOIS O PROGRAMA VOLTA A SER AUTOMÁTICO 
time.sleep(10)

addfriend = driver.find_element(By.XPATH, '//*[@id="pagecontent"]/div[2]/div[1]/a[2]/span')
addfriend.click()

time.sleep(2)

numberfriend = driver.find_element(By.XPATH, '//*[@id="application_root"]/div[2]/div[2]/div[2]/div/input')
numberfriend.send_keys('12312312312312')

time.sleep(2)

driver.close()




