import pytest
from selenium import webdriver


# Fixture to initialize the Selenium WebDriver
@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser", default="chrome").lower()
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Run Chrome in headless mode
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Invalid browser specified: {browser_name}")
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser for testing")
