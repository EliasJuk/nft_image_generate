from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')

# INSTALAR EXTENÇÃO
chrome_options = ChromeOptions()
chrome_options.add_extension('extension.crx')
driver = webdriver.Chrome('./chromedriver', options=chrome_options)
driver.execute_script("window.open('http://google.com/', '_blank')")
driver.close()

def metamask():
  # Muda de aba
  time.sleep(2)
  driver.switch_to.window(driver.window_handles[0])
  driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/button').click()

  # Carteira
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()


  # Termos
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()

  # Frase Secreta
  time.sleep(2)
  frase_secreta = config['metamask']['secret']
  driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input').send_keys(frase_secreta)

  # Senha
  time.sleep(2)
  senha = config['metamask']['key']
  driver.find_element_by_xpath('//*[@id="password"]').send_keys(senha)

  # Confirm
  time.sleep(2)
  driver.find_element_by_xpath('//*[@id="confirm-password"]').send_keys(senha)

  # Termos
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div').click()

  # Import
  time.sleep(1)
  driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/button').click()

def mintable():
  time.sleep(4)
  driver.switch_to.window(driver.window_handles[1])

  # Mintable
  driver.get('https://mintable.app/')

  # Login
  driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[1]/button[1]').click()

  # User
  User = driver.find_element_by_xpath('//*[@id="modals-root"]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/div[2]/input')
  User.send_keys(config['mintable']['user'])

  # Password
  Pass = driver.find_element_by_xpath('//*[@id="modals-root"]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div[2]/input')
  Pass.send_keys(config['mintable']['key'])

  # Log In
  driver.find_element_by_xpath('//*[@id="modals-root"]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/form/div[2]/div/div[2]/input').send_keys(Keys.ENTER)


metamask()