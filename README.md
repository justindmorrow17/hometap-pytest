# hometap-pytest
README for Interest Rate Input Testing

Overview
This repository contains automated tests for verifying the functionality of the interest rate input field and the legal disclaimer on the Zillow mortgage calculator webpage. The tests are written in Python using the Selenium WebDriver and the unittest framework.

Prerequisites
Before running the tests, ensure you have the following installed:

Python 3.x
Selenium library
Chrome WebDriver
Installation
Clone the repository:
git clone https://github.com/justindmorrow17/hometap-pytest.git

Install the required Python packages:
pip install selenium
Download the Chrome WebDriver:
Download the WebDriver from the official site that matches your Chrome browser version.
Ensure the WebDriver executable is in your system's PATH or place it in the project directory.

Test Cases
The test suite includes the following test cases:

1. Verify the Interest Rate Input Accepts Valid Numerical Values
This test ensures that the interest rate input field accepts valid numerical values.

def test_valid_interest_rate(self):
    driver = self.driver
    interest_rate_input = driver.find_element(By.ID, "rate")
    interest_rate_input.clear()
    interest_rate_input.send_keys("4.5")
    self.assertEqual(interest_rate_input.get_attribute("value"), "4.5")
    
2. Verify the Interest Rate Input Does Not Accept Non-Numerical Values
This test ensures that the interest rate input field does not accept non-numerical values and displays the appropriate error message.

def test_invalid_non_numerical_interest_rate(self):
    driver = self.driver
    interest_rate_input = driver.find_element(By.ID, "rate")
    interest_rate_input.clear()
    interest_rate_input.send_keys("abc")
    element = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]")
    element.click()
    abc_error_message = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/p[1]").text
    abc_expected_message = "'abc' is not a valid number"
    assert abc_error_message == abc_expected_message, f"Expected '{abc_expected_message}' but got '{abc_error_message}'"
   
4. Verify the Functionality and Accuracy of the Legal Disclaimer
This test ensures that the legal disclaimer modal is displayed correctly and contains the expected text.

def test_legal_disclaimer(self):
    driver = self.driver
    disclaimer_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Calculator disclaimer')]")
    disclaimer_btn.click()
    disclaimer_modal_message = driver.find_element(By.XPATH, "//p[contains(text(), 'The mortgage calculator is intended to be used for educational purposes only.')]").text
    expected_message = "The mortgage calculator is intended to be used for educational purposes only. Actual available rates and monthly payment amounts are subject to market fluctuations and will depend on a number of factors, including geography and loan characteristics. The estimates are based on information you provide, and may not include other fees and costs that a lender may assess in addition to monthly principal and interest, such as taxes and insurance and the actual payment obligation may be greater. Zillow Group Marketplace, Inc. does not make loans and this is not a commitment to lend."
    assert disclaimer_modal_message == expected_message, f"Expected '{expected_message}' but got '{disclaimer_modal_message}'"

Running the Tests
The tests were built using the Pycharm Community Edition IDE
To run the tests, execute the following command:
pytest -rA -v 

File Structure
test_interest_rate_input.py: Contains the test cases for verifying the interest rate input and the legal disclaimer.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
