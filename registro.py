from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
Service = Service()
options = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=Service,options=options)

browser.get('https://demo.automationtesting.in/Register.html')
#firstname
browser.find_element(By.CLASS_NAME,'form-control').send_keys('Anderson')
#last name
browser.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys('Filho')
# Address
browser.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[2]/div/textarea').send_keys('Gosto de ler sobre curiosidade do mundo')
#Email
browser.find_element(By.XPATH,'//*[@id="eid"]/input').send_keys('larita@larita.com')
#number
browser.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[4]/div/input').send_keys('(81) 981379321')
#gender
browser.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()
#hobies
browser.find_element(By.ID,'checkbox2').click()
#linguagens
browser.find_element(By.ID,'msdd').click()
browser.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[29]/a').click()
#Skils
browser.find_element(By.XPATH,'//*[@id="Skills"]/option[61]').click()
#COntry 
browser.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[10]/div/span/span[1]/span').click()
  
#date
browser.find_element(By.ID,'yearbox').send_keys('2003')
browser.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[11]/div[2]/select/option[8]').click()
browser.find_element(By.XPATH,'//*[@id="daybox"]/option[22]').click()
#senhas
browser.find_element(By.ID,'firstpassword').send_keys('Senha')
browser.find_element(By.ID,'secondpassword').send_keys('Senha')
browser.save_screenshot('prova.png')



# pais = browser.find_element(By.XPATH,"//ul[@class='ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all']")
# lista_elementos = pais.find_elements(By.XPATH,".//li[@class='ng-scope']/a")
# for elementos in lista_elementos:
#     print(elementos.get_attribute('textContent'))


