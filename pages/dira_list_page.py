import time

from selenium.webdriver.common.by import By

from .base_page import BasePage
from utils.csvhandler import create_csv


class DiraListPage(BasePage):
    TABLE_LOCATOR = "//*[@id='divView']/div/div[7]/div/div[1]/table"
    TITLES_LOCATOR = TABLE_LOCATOR + "/thead/tr"
    ROWS_LOCATOR = TABLE_LOCATOR + "/tbody/tr"
    NEXT_PAGE_LOCATOR = "//*[contains(text(), '»')]"
    DATA_BY_TITLES = {
        "מספר הגרלה": [],
        "זכאות": [],
        "סיום הרשמה": [],
        "יישוב": [],
        "קבלן": [],
        "דירות בהגרלה": [],
        "מתוכם דירות לבני מקום": [],
        "נרשמים בהגרלה": [],
        "מתוכם נרשמים בני מקום": [],
        "מחיר למטר": [],
        "מענק": []
    }

    def __init__(self, driver):
        super().__init__(driver)

    def export_data_list_from_table(self, pages):
        for page in range(pages):
            for title in self.DATA_BY_TITLES.keys():
                elements = self.find_elements_by_xpath(self.ROWS_LOCATOR + f'/td[contains(@data-title, "{title}")]')
                for element in elements:
                    self.DATA_BY_TITLES[title].append(element.get_attribute("innerText"))
            self.click_on_element(self.NEXT_PAGE_LOCATOR)
            time.sleep(5)
        create_csv(self.DATA_BY_TITLES)
