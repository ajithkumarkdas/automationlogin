from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from getpass import getpass

userName = os.environ['ajithkumar_O5LtPf']
accessKey = os.environ['chDzgheXDyQmy95wW4GQ']
localIdentifier = os.environ['BROWSERSTACK_LOCAL_IDENTIFIER']
buildName = os.environ['Build 1']
projectName = os.environ['Sample sandbox project']

desired_cap = {
'bstack:options' : {
"os" : "Windows",
"osVersion" : "10",
"buildName" : "BStack Build Name: " + buildName,
"projectName" : "BStack Project Name: " + projectName,
 "localIdentifier": localIdentifier,
        "seleniumVersion" : "4.0.0",
        "userName": ajithkumar_O5LtPf,
        "accessKey": chDzgheXDyQmy95wW4GQ
},
"browserName" : "Chrome",
"browserVersion" : "latest",
}

options = ChromeOptions()
options.set_capability('bstack:options', bstack_options)
driver = webdriver.Remote(
    command_executor="https://hub.browserstack.com/wd/hub",
    options=options)

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
print(driver.title)
driver.quit()
