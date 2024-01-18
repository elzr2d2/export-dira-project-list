import time

import pandas
from .base_page import BasePage


def get_text_list_from_elements(elements):
    text_list = []
    for element in elements:
        text_list.append(element.text)
    print(text_list)
    return text_list


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.dira.moch.gov.il/ProjectsList"
        self.table_locator = "//*[@id='divView']/div/div[7]/div/div[1]/table"
        self.titles_locator = self.table_locator + "/thead/tr"
        self.rows_locator = self.table_locator + "/tbody/tr"
        self.cells_locator = self.rows_locator + "/td[@class='ng-binding']"
        self.next_page_locator = "//*[contains(text(), '»')]"
        self.data_titles = {
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

    def get_data_list_from_table(self, pages):
        for page in range(pages):
            for title in self.data_titles.keys():
                elements = self.find_elements_by_xpath(self.rows_locator + f'/td[contains(@data-title, "{title}")]')
                for element in elements:
                    self.data_titles[title].append(element.get_attribute("innerText"))
            self.click_on_element(self.next_page_locator)
            time.sleep(5)
        return self.data_titles

    def create_csv(self, list_to_csv):
        pandas.DataFrame(list_to_csv).to_csv("../exported_data/dira_table.csv")
