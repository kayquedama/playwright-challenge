# Playwrite challenge

This project contains a set of files and directories for testing a web application using Playwright and Pytest.

## Project Structure

The project is organized into the following folders and files:

### Folders

1. **Pages**
   - Contains Python files that define the functions of the web pages used in the tests. These functions represent interactions and behaviors that can be performed on various pages of the web application.

2. **Report**
   - Stores reports generated from the execution of the tests. These reports provide detailed insights into the results of each test run, helping to track test status and issues.

3. **Tests**
   - Contains all the test files that define the test cases for the web application. These tests are executed using Pytest and Playwright.

4. **Utilities**
   - Holds utility scripts and functions that are designed to be used across different test cases. These utilities are intended to support testing operations like data preparation, common setup tasks, or helper functions.

### Files

1. **config.json**
   - Configuration file for Playwright. This file holds important configurations like browser settings, timeouts, and other options necessary to set up and run Playwright.

2. **conftest.py**
   - This file contains the initial setup for the tests, including fixture definitions and hooks that need to be applied globally across the test suite. This may include session-level setup, test data, or browser configurations.

3. **pytest.ini**
   - Configuration file for Pytest. This file specifies the pytest commands and options to control test execution, output formatting, and other pytest-related settings.

## Setup

### Prerequisites

To set up this project, you need to have the following installed:

- Python (preferably 3.8 or higher)
- Playwright
- Pytest
- Pytest Report

### Installation

1. Clone the repository:

2. Intall Requiriments
`pip install - requiriments.txt`
3. Install playwright
`playwright install`
4. Put the username and password in config.json file

5. Run Pytest
`pytest`
6. Check Report
