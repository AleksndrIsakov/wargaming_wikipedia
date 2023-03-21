import re
import pytest
from src.table_data import Table, Column
from src.table_page import TablePage
from selenium import webdriver


class TestTable:
    testdata = [pow(10, 7), 1.5 * pow(10, 7), 5 * pow(10, 7), pow(10, 8), 5 * pow(10, 8), pow(10, 9), 1.5 * pow(10, 9)]

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        TablePage(cls.driver).open().read_table()

    @pytest.mark.parametrize("test_input", testdata)
    def test_expected_visitors(self, test_input):
        err_lines = Table()
        for row in Table.rows:
            popularity = self.string_to_float(row.cells[Column.POPULARITY])
            if test_input > popularity:
                err_lines.rows.append(row);

        err_msg = "\n"
        for row in err_lines.rows:
            err_msg += ("{} (Frontend: {} | Backend: {}) has {:.0f} unique visitors per month.(Expected more than {:.0f})\n".format(
                self.remove_ref(row.cells[Column.WEBSITES]),
                self.remove_ref(row.cells[Column.FRONTEND]),
                self.remove_ref(row.cells[Column.BACKEND]),
                self.string_to_float(row.cells[Column.POPULARITY]),
                test_input))

        if len(err_lines.rows) > 0:
            raise(AssertionError(err_msg))

    @classmethod
    def teardown_class(cls):
        cls.driver.close()

    def string_to_float(self, string: str):
        return float(re.sub("\\D", '', self.remove_ref(string)))

    def remove_ref(self, string):
        return re.sub("\\[\\d*\\]", '', string)