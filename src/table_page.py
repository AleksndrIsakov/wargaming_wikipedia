from selenium.webdriver.common.by import By
from src.base_page import BasePage, _BASE_URL
from src.table_data import Table, Row


class TablePage(BasePage):
    url = _BASE_URL + "/wiki/Programming_languages_used_in_most_popular_websites"

    table = (By.XPATH, ".//caption[contains(text(),'Programming languages')]/parent::table")
    row = (By.XPATH, "./tbody/tr")
    cell = (By.XPATH, "./td")

    def read_table(self):
        web_tbl = self.driver.find_element(*self.table)

        Table.rows = []
        rows = web_tbl.find_elements(*self.row)
        for row in rows:
            cells = row.find_elements(*self.cell)
            text = list(map(lambda x: x.text, cells))
            Table.rows.append(Row(text))
