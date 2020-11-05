from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = "Your Mail"
password = "Your Pass"

getdriver = ("https://www.instagram.com")

driver = webdriver.Firefox()
driver.get(getdriver)
html = driver.page_source
time.sleep(2)

driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
time.sleep(5)

driver.get("https://www.instagram.com/")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()

x = 0
for x in range(5):
    driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[1]/div[2]/div/article[" + str((x%10)+1) + "]/div[3]/section[1]/span[1]/button").click()
    time.sleep(1)
driver.close()


