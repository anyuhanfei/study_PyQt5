'''
269-QCalendarWidget-日期范围

API:
    setMinimumDate(QDate date) -- 设置最小日期, 默认为 -4714
    minimumDate() -> QDate -- 获取最小日期
    setMaximumDate(QDate date) -- 设置最大日期, 默认为 9999
    maximumDate() -> QDate -- 获取最大日期
    setDateRange(QDate min, QDate max) -- 设置日期区间
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget
from PyQt5.QtCore import QDate


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('269-QCalendarWidget-日期范围')
        self.resize(1000, 500)

        cw = QCalendarWidget(self)

        '''设置最大日期'''
        cw.setMaximumDate(QDate(2022, 12, 31))
        '''设置最小日期'''
        cw.setMinimumDate(QDate(2020, 1, 1))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
