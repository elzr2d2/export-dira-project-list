import pandas

from pages.dira_list_page import DiraListPage


def test_export_data_from_dira_as_csv(browser):
    browser.get("https://www.dira.moch.gov.il/ProjectsList")
    dlp = DiraListPage(browser)
    dlp.export_data_list_from_table(pages=2)

    assert True
