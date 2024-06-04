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
  
2. Verify the Interest Rate Input Does Not Accept Non-Numerical Values
This test ensures that the interest rate input field does not accept non-numerical values and displays the appropriate error message.
   
3. Verify the Functionality and Accuracy of the Legal Disclaimer
This test ensures that the legal disclaimer modal is displayed correctly and contains the expected text.

Running the Tests
The tests were built using the Pycharm Community Edition IDE
To run the tests, execute the following command:
pytest -rA -v 

File Structure
test_interest_rate_input.py: Contains the test cases for verifying the interest rate input and the legal disclaimer.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
