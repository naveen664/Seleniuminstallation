from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

#Github Credinatials
username = os.getenv("GIT-USER")
password = os.getenv("GIT-PWD")

# instialize the Chrome driver
driver = webdriver.Chrome(r"chromedriver")
# head to github login page
driver.get("https://github.com/login/")
# find username/email field and send the username itself to the input field
driver.find_element("id", "login_field").send_keys(username)
# findpassword input field and insert password as well
driver.find_element("id", "password").send_keys(password)
# click login button
driver.find_element("name", "commit").click()
# wait the ready state to be complete
WebDriverWait(driver=driver, timeout=20).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
    )
error_message = "Incorrect username or password"
# get the errors (if there are)
errors = driver.find_elements("css selector", ".flash-error")
# print the errors optionally
# for e in error:
#     print(e.text)
# if we find the error message within errors, then login is failed
if any(error_message in e.text for e in errors):
      print("[!] Login failed")
else:
      print("[+] Login successful")

# an example scenario, show me my public repositories
repos = driver.find_element("css selector", ".js-repos-container")
# wait for the repos container to be loaded
WebDriverWait(driver=driver, timeout=20).until((lambda x: repos.text != "Loading..."))
# iterate over the repos and print their names
for repo in repos.find_elements("css selector", "li.public"): # you can use "li.privates" for privates repo
      print(repo.find_element("css selector", "a").get_attribute("href")) 

# close the driver 
driver.close()