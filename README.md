# Selenium Automation for SauceDemo

## Overview
This project is a Selenium automation script for testing the checkout process on the SauceDemo website. The script performs the following actions:

1. Launches a Chrome browser and navigates to SauceDemo.
2. Logs in using provided credentials.
3. Adds multiple items to the shopping cart.
4. Proceeds to checkout and enters billing information.
5. Completes the purchase and returns to the product page.

## Prerequisites
Ensure you have the following installed on your system before running the script:

- Python (>= 3.x)
- Google Chrome (latest version)
- ChromeDriver (compatible with your Chrome version)
- Selenium WebDriver (`pip install selenium`)

## Installation
1. Clone this repository or copy the script.
2. Install required dependencies using:
   ```sh
   pip install selenium
   ```
3. Ensure ChromeDriver is installed and added to your system PATH.

## Usage
1. Save the script as `saucedemo_test.py`.
2. Run the script using:
   ```sh
   python saucedemo_test.py
   ```
3. The script will execute the login, add items to the cart, complete the checkout process, and return to the product page.

## Code Breakdown
- **Variable Declarations:** Stores login credentials, URLs, and user information.
- **Browser Initialization:** Opens Chrome and navigates to SauceDemo.
- **Login Process:** Enters credentials and logs in.
- **Adding Items to Cart:** Selects three products and adds them to the cart.
- **Checkout Process:** Fills in user details and completes the purchase.
- **Completion:** Returns to the product page and closes the browser.

---
## Author
Richard Akintunde

## License
This project is open-source and available for personal and educational use.



