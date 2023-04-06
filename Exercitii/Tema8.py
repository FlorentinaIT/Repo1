from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome = webdriver.Chrome()

# Identificare dupa ID

# chrome.get('https://formy-project.herokuapp.com/form')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# el1 = chrome.find_element(By.ID, 'first-name')
# time.sleep(3)
# el1.send_keys("Florentina")
# time.sleep(3)

# chrome.get('https://formy-project.herokuapp.com/')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# logo = chrome.find_element(By.ID, "logo")
# time.sleep(3)

# chrome.get('https://formy-project.herokuapp.com/form')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# chrome.find_element(By.ID, "job-title").send_keys('economist')
# time.sleep(3)

# Identificare dupa Link_Text

# chrome.get('https://formy-project.herokuapp.com')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# el2 = chrome.find_element(By.LINK_TEXT, 'Buttons')
# el2.click()
# time.sleep(3)

# chrome.get('https://formy-project.herokuapp.com')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# autocomplete = chrome.find_element(By.LINK_TEXT, 'Autocomplete')
# autocomplete.click()
# time.sleep(3)

# chrome.get('https://formy-project.herokuapp.com')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# datepicker = chrome.find_element(By.LINK_TEXT, 'Datepicker')
# datepicker.click()
# time.sleep(3)

# Identificare dupa Partial Link text

# chrome.get('https://formy-project.herokuapp.com')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# el3 = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Key')
# el3.click()
# time.sleep(3)

# chrome.get('https://formy-project.herokuapp.com/')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# enabled = chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enabled')
# enabled.click()
# time.sleep(3)

# chrome.get('https://formy-project.herokuapp.com/')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# file = chrome.find_element(By.PARTIAL_LINK_TEXT, 'File')
# file.click()
# time.sleep(3)

# Identificare dupa Name

# chrome.get('https://the-internet.herokuapp.com/login')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# chrome.find_element(By.NAME, 'username').send_keys('Florentina')
# time.sleep(3)
# chrome.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
# time.sleep(3)

# Identificare dupa Tag

# chrome.get('https://the-internet.herokuapp.com/login')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# tag1 = chrome.find_elements(By.TAG_NAME, 'input')
# tag1[0].send_keys('tomsmith')
# time.sleep(3)
# tag1[1].send_keys('SuperSecretPassword!')
# time.sleep(3)

# chrome.get('https://formy-project.herokuapp.com/buttons')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# tag2 = chrome.find_elements(By.TAG_NAME, 'button')
# tag2[1].click()
# time.sleep(3)


# Identificare dupa Class name

# chrome = webdriver.Chrome()
# chrome.get("https://formy-project.herokuapp.com/autocomplete")
# time.sleep(2)
#
# chrome.maximize_window()
# time.sleep(2)
#
# el4 = chrome.find_elements(By.CLASS_NAME, 'form-control')
# el4[6].send_keys('Romania')
# time.sleep(3)
#
# el5 = chrome.find_elements(By.CLASS_NAME, 'form-control')
# el5[3].send_keys('Bucuresti')
# time.sleep(3)
#
# el6 = chrome.find_elements(By.CLASS_NAME, 'form-control')
# el6[1].send_keys('D-dul Unirii')
# time.sleep(3)

# chrome.get('https://the-internet.herokuapp.com/login')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# tag1 = chrome.find_elements(By.TAG_NAME, 'input')
# tag1[0].send_keys('tomsmith')
# time.sleep(3)
# tag1[1].send_keys('SuperSecretPassword!')
# time.sleep(3)
# el7 = chrome.find_element(By.CLASS_NAME, 'radius')
# el7.click()
# time.sleep(3)


# chrome.get('https://formy-project.herokuapp.com/')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# button = chrome.find_elements(By.CLASS_NAME, "btn btn-lg")
# time.sleep(3)

# Identificare dupa CSS SELECTORS:


# chrome.get('https://the-internet.herokuapp.com/login')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# tag1 = chrome.find_elements(By.TAG_NAME, 'input')
# identificare CSS_SELECTOR dupa ID
# tag1 = chrome.find_elements(By.CSS_SELECTOR, '#username')
# tag1[0].send_keys('tomsmith')
# time.sleep(3)
# tag1[1].send_keys('SuperSecretPassword!')
# time.sleep(3)
# el7 = chrome.find_element(By.CLASS_NAME, 'radius')
# el7.click()
# time.sleep(3)
#identificare dupa tag + atribut cheie - valoare
# logout = chrome.find_element(By.CSS_SELECTOR, 'a[class = "button secondary radius"]')
# time.sleep(3)
# logout.click()
# time.sleep(3)
#identificare dupa clasa
# chrome.get('https://phptravels.net/')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# hotel = chrome.find_elements(By.CSS_SELECTOR, '.text')
# time.sleep(3)
# hotel[0].click()
# time.sleep(3)
#identificare dupa atribut=valoare partiala
# chrome.get('https://phptravels.net/')
# time.sleep(3)
# chrome.maximize_window()
# time.sleep(3)
# flight = chrome.find_elements(By.CSS_SELECTOR, '.text')
# time.sleep(3)
# flight[1].click()
# time.sleep(3)