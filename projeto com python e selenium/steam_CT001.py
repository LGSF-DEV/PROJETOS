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
#preencher a barra de pesquisa com o nome de um jogo para maior de 17
navegacao = driver.find_element(By.NAME, 'term') 
navegacao.send_keys('Batman Arkham Knight')

time.sleep(2)
#clickar em pesquisar
pesquisar = driver.find_element(By.XPATH, '//*[@id="store_search_link"]/img')
pesquisar.click()

time.sleep(2)
#clickar na imagem do jogo para ser direcionado para o jogo
batman = driver.find_element(By.XPATH, '//*[@id="search_resultsRows"]/a[1]/div[1]/img')
batman.click()

time.sleep(2)
#clickar no campo idade
ageday = driver.find_element(By.ID, 'ageDay')
ageday.click()

time.sleep(2)
#selecionar o dia do nascimento
day = driver.find_element(By.XPATH, '//*[@id="ageDay"]/option[29]')
day.click()

time.sleep(2)
#clickar no campo mês 
agemonth = driver.find_element(By.ID, 'ageMonth')
agemonth.click()

time.sleep(2)
#colocar o mês de nascimento
month = driver.find_element(By.XPATH, '//*[@id="ageMonth"]/option[2]')
month.click()

time.sleep(2)
#clickar no campo ano
ageyear = driver.find_element(By.ID, 'ageYear')
ageyear.click()

time.sleep(2)
#colocar o ano de nascimento
year = driver.find_element(By.XPATH, '//*[@id="ageYear"]/option[111]')
year.click()

time.sleep(2)
#clickar em acessar página
acessarjogo = driver.find_element(By.XPATH, '//*[@id="view_product_page_btn"]/span')
acessarjogo.click()

time.sleep(5)

driver.close()
