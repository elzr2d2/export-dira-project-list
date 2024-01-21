import pytest
from selenium import webdriver


class WebDriverWrapper:
    def __init__(self, browser_name):
        self.browser_name = browser_name.lower()
        self.driver = None

    def __enter__(self):
        if self.browser_name == "chrome":
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")  # Run Chrome in headless mode
            self.driver = webdriver.Chrome(options=options)
        elif self.browser_name == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError(f"Invalid browser specified: {self.browser_name}")
        self.driver.implicitly_wait(15)
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser", default="chrome")
    with WebDriverWrapper(browser_name) as driver:
        yield driver
