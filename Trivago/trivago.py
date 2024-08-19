from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


# Configura o serviço do ChromeDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.trivago.com.br/')

navegador.find_element(By.XPATH, "//input[contains(@autocapitalize,'off')]").send_keys('Manaus')
navegador.find_element(By.XPATH, "//button[@type='button'][contains(.,'Pesquisar')]").click()

find_sorting_selector = navegador.find_element(By.XPATH, "//select[contains(@class,'SortingSelector_select__usK9k Select_select__7NVo3 truncate_truncate__vCzPM')]")
select_sorting_selector = Select(find_sorting_selector)
select_sorting_selector.select_by_visible_text('Avaliação e sugestões')

first_name_result = navegador.find_element(By.CSS_SELECTOR, 'li[data-testid="accommodation-list-element"]:first-child h2 span')
print(first_name_result.text)

first_starts_result = navegador.find_element(By.CSS_SELECTOR, 'div[class="StandardDatesArea_priceContainer__jpIZs"]: first-child span b')
if first_starts_result:
    print("Elemento encontrado.")
    
first_value_result = navegador.find_element
(By.CSS_SELECTOR, 'div[class="info-section_infoSection__sY1hr info-section_margin__rNbKo"]>div[class="AccommodationType_hotelClass__O1Wnl"] button')
print(first_value_result.text)

navegador.quit()