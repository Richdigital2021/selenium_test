import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Variable declaration
wait = 5
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
first_name = "Richard"
last_name = "Akintunde"

#Browser initialization
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(wait)

#
UserName = driver.find_element(By.ID, "user-name")
UserName.send_keys(username)

PassWord = driver.find_element(By.ID, "password")
PassWord.send_keys(password)

Login = driver.find_element(By.ID, "login-button")
Login.click()
time.sleep(wait)

# Adding Items to Cart
BackPack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
BackPack.click()

BikeLight = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
BikeLight.click()

T_Shirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
T_Shirt.click()

ShoppingContainer = driver.find_element(By.ID, "shopping_cart_container")
ShoppingContainer.click()
time.sleep(wait)

# The checkout process
CheckOut = driver.find_element(By.ID, "checkout")
CheckOut.click()
time.sleep(wait)

# Entering Billing Information
driver.find_element(By.ID, "first-name").send_keys("Richard")
driver.find_element(By.ID, "last-name").send_keys("Akin")
driver.find_element(By.ID, "postal-code").send_keys("234567")
time.sleep(wait)

# Finish shopping
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()
time.sleep(wait)

# Go back to products page
driver.find_element(By.ID, "back-to-products").click()

time.sleep(wait)


