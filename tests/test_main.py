from pages.login_page import LoginPage


def test_export_data_from_dira_as_csv(browser):
    browser.get("https://www.dira.moch.gov.il/ProjectsList")
    lp = LoginPage(browser)
    data = lp.get_data_list_from_table(pages=2)     # <-- change number for more pages to be scraped
    lp.create_csv(data)

    assert True
