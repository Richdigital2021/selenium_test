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
postalcode = "234567"

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
FirstName = driver.find_element(By.ID, "first-name")
FirstName.send_keys("first_name")

LastName = driver.find_element(By.ID, "last-name")
LastName.send_keys("last_name")

PostalCode = driver.find_element(By.ID, "postal-code")
PostalCode.send_keys("postalcode")
time.sleep(wait)

# Finish shopping
Continue = driver.find_element(By.ID, "continue")
Continue.click()
time.sleep(wait)

Finish = driver.find_element(By.ID, "finish")
Finish.click()
time.sleep(wait)

# Go back to products page
BackToProducts = driver.find_element(By.ID, "back-to-products")
BackToProducts.click()

time.sleep(wait)


