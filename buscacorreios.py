from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get(https://www2.correios.com.br/sistemas/buscacep/buscaCepEndereco.cfm)

navegador.find_element('xpath', //a[contains(.,'Endereço por CEP')]).click()
navegador.find_element(By.ID, 'cep').send_keys(69005-040)
