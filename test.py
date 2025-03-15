import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(5)

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(5)
driver.find_element(By.ID, "checkout").click()
time.sleep(5)
driver.find_element(By.ID, "first-name").send_keys("Richard")
driver.find_element(By.ID, "last-name").send_keys("Akin")
driver.find_element(By.ID, "postal-code").send_keys("234567")
time.sleep(5)
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
time.sleep(5)
driver.find_element(By.ID, "back-to-products").click()

time.sleep(20)


