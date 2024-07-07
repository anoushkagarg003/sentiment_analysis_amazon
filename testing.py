from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your Firefox WebDriver executable
# Make sure you have geckodriver installed: https://github.com/mozilla/geckodriver/releases
geckodriver_path = r"C:\Users\anous\Downloads\geckodriver-v0.33.0-win64\geckodriver.exe"

firefox_options = webdriver.FirefoxOptions()
# Optional: Run in headless mode
# firefox_options.add_argument("--headless")

# Set the path to geckodriver
driver = webdriver.Firefox()
driver.get("https://vtop.vit.ac.in/vtop/login")
try:
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.fw-bold")))
    button.click()
    print("Button clicked successfully!")
except Exception as e:
    print("Failed to click the button:", e)
try:
    # Wait for the username input field to be visible
    username_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )

    # Find password input field
    password_input = driver.find_element_by_id("password")

    # Find submit button
    submit_button = driver.find_element_by_id("submitBtn")

    # Enter username and password
    username_input.send_keys("your_username")
    password_input.send_keys("your_password")

    # Click on the submit button
    submit_button.click()

    # Wait for the page to load or for a redirect to happen
    # You can add explicit waits here if necessary

    # Verify if login was successful (you can check for elements on the next page)

except NoSuchElementException:
    print("Element not found. Please check your selectors.")
except ElementClickInterceptedException:
    print("Element is not clickable. Please check if it's covered by another element.")
finally:
    # Close the browser
    driver.quit()
