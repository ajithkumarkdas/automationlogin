from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

username = input("ajithkumarkdas@gmail.com")
password = getpass("Devi@1970")

SignIn_button = driver.find_element("xpath", '//*[@id="nav-link-accountList"]/span')
SignIn_button.click()
username_textbox = driver.find_element_by_id("ap_email")
username_textbox.send_keys(username)
Continue_button = driver.find_element_by_id("continue")
Continue_button.submit()
password_textbox = driver.find_element_by_id("ap_password")
password_textbox.send_keys(password)
SignIn_button = driver.find_element_by_id("auth-signin-button-announce")
SignIn_button.submit()
