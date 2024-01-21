from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    INNER_TEXT = "innerText"

    def __init__(self, driver):
        self.driver = driver

    def wait_for_elements(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((by, value))
        )

    def wait_for_element(self, by, value, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def get_text(self, xpath):
        return self.find_element_by_xpath(xpath).text

    def find_element_by_xpath(self, xpath):
        return self.wait_for_element(By.XPATH, xpath)

    def find_elements_by_xpath(self, xpath):
        return self.wait_for_elements(By.XPATH, xpath)

    def get_attribute(self, xpath, attribute):
        return self.find_element_by_xpath(xpath).get_attribute(attribute)

    def get_inner_text_attribute(self, xpath):
        return self.get_attribute(xpath, self.INNER_TEXT)

    def click_on_element(self, xpath):
        return self.find_element_by_xpath(xpath).click()
