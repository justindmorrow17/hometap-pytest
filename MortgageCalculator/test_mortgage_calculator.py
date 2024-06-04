from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestInterestRateInput(unittest.TestCase):
    def setUp(self):
        # Initializes the Chrome WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.zillow.com/mortgage-calculator/")

#Test Case 1: Verify the Interest Rate input accepts valid numerical values
    def test_valid_interest_rate(self):
        driver = self.driver
        interest_rate_input = driver.find_element(By.ID, "rate")
        interest_rate_input.clear()
        interest_rate_input.send_keys("4.5")
        # Add assertion to check the input value
        self.assertEqual(interest_rate_input.get_attribute("value"), "4.5")

# Test Case 5: Verify the Interest Rate input does not accept non-numerical values
    def test_invalid_non_numerical_interest_rate(self):
        driver = self.driver
        # Identify interest rate input and send "abc"
        interest_rate_input = driver.find_element(By.ID, "rate")
        interest_rate_input.clear()
        interest_rate_input.send_keys("abc")

        # Click the element, workaround to bypass Testing Note 12.5
        element = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]")
        element.click()

        # Add assertion to check for abc error message
        abc_error_message = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/p[1]").text
        # print(abc_error_message) test validation for the value of the error message
        abc_expected_message = "'abc' is not a valid number"
        assert abc_error_message == abc_expected_message, f"Expected '{abc_expected_message}' but got '{abc_error_message}'"

#Test Case 8: Verify the functionality and accuracy of the Legal Disclaimer
    def test_legal_disclaimer(self):
        driver = self.driver
        # Click the legal disclaimer button
        disclaimer_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Calculator disclaimer')]")
        disclaimer_btn.click()

        # Validating the disclaimer message
        disclaimer_modal_message = driver.find_element(By.XPATH, "//p[contains(text(), 'The mortgage calculator is intended to be used for educational purposes only.')]").text  # Adjust the selector as necessary
        # print(disclaimer_modal_message) test validation for the value of the error message
        expected_message = "The mortgage calculator is intended to be used for educational purposes only. Actual available rates and monthly payment amounts are subject to market fluctuations and will depend on a number of factors, including geography and loan characteristics. The estimates are based on information you provide, and may not include other fees and costs that a lender may assess in addition to monthly principal and interest, such as taxes and insurance and the actual payment obligation may be greater. Zillow Group Marketplace, Inc. does not make loans and this is not a commitment to lend."
        assert disclaimer_modal_message == expected_message, f"Expected '{expected_message}' but got '{disclaimer_modal_message}'"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()