from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass

BROWSERSTACK_URL = 'https://ajithkumar_O5LtPf:chDzgheXDyQmy95wW4GQ@hub-cloud.browserstack.com/wd/hub'

desired_cap = {
'bstack:options' : {
"os" : "Windows",
"osVersion" : "10",
"projectName" : "Sample sandbox project",
"buildName" : "Build #1",
"sessionName" : "My First Test",
},
"browserName" : "Chrome",
"browserVersion" : "latest",
}

driver = webdriver.Remote(
    command_executor=BROWSERSTACK_URL,
    desired_capabilities=desired_cap
)

driver.get("https://www.amazon.in")

username = input("Enter in your username: ")
password = getpass("Enter in your password: ")
SignIn_button = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
SignIn_button.click()
username_textbox = driver.find_element_by_id("ap_email")
username_textbox.send_keys(username)
Continue_button = driver.find_element_by_id("continue")
Continue_button.submit()
password_textbox = driver.find_element_by_id("ap_password")
password_textbox.send_keys(password)
SignIn_button = driver.find_element_by_id("auth-signin-button-announce")
SignIn_button.submit()

driver.quit()
