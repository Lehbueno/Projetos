from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.trivago.com.br/')

sleep(5)

navegador.find_element('xpath', "//input[contains(@autocapitalize,'off')]").send_keys('Manaus')
navegador.find_element('xpath', "//button[@type='button'][contains(.,'Pesquisar')]").click()

find_sorting_selector = \
navegador.find_element('xpath', "//select[contains(@class,'SortingSelector_select__usK9k Select_select__7NVo3 truncate_truncate__vCzPM')]").click()
select_sorting_selector = Select(find_sorting_selector)
select_sorting_selector.select_by_visible_text('Avaliação e sugestões')

sleep(5)

first_result = navegador.find_element(By.CSS_SELECTOR, 'li[data-testid="accommodation-list-element"]:first-child h2 span')
for e in first_result:
    print(e.text)