from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

# INSTALAR EXTENÇÃO
chrome_options = ChromeOptions()
chrome_options.add_extension('extension.crx')
driver = webdriver.Chrome('./chromedriver', options=chrome_options)


# FECHAR NAVEGADOR
input('Press [ENTER] to close browser...')
driver.quit()