from selenium import webdriver
from getpass import getpass

usr = input("SEU USER/EMAIL: ")
pwd = getpass('SUA SENHA: ')

driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

usr_box = driver.find_element_by_class_name("js-username-field email-input js-initial-focus")
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_class_name("js-password-field")
pwd_box.send_keys(pwd)

login_button = driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")  
login_button.submit()
