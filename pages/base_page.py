from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_elements(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def get_text(self, value):
        return self.find_element_by_xpath(value).text

    def find_element_by_xpath(self, xpath, timeout=10):
        return self.wait_for_element(By.XPATH, xpath, timeout)

    def find_elements_by_xpath(self, xpath, timeout=10):
        return self.wait_for_elements(By.XPATH, xpath, timeout)

    def click_on_element(self, xpath):
        return self.find_element_by_xpath(xpath).click()
