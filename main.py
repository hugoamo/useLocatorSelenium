from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.gmail.com")


## Localizadores por ID

inputShearch = driver.find_element(by=By.ID, value="identifierId")
print(inputShearch.get_attribute("autocomplete"))

## Localizadores por NAME

inputShearchName=driver.find_element(by=By.NAME, value="identifier")
print(inputShearchName.get_attribute("type"))

## Localizador por Xpath relativo
inputShearchXpath=driver.find_element(by=By.XPATH, value="//input[@id='identifierId']")
print(inputShearchXpath.get_attribute("dir"))

## Localizador por Css Selector
inputShearchCss=driver.find_element(by=By.CSS_SELECTOR, value="#identifierId")
print(inputShearchCss.get_attribute("spellcheck"))


## Localizador por Class
inputShearchClass=driver.find_element(by=By.CLASS_NAME, value="whsOnd zHQkBf")
print(inputShearchClass.get_attribute("jsname"))



