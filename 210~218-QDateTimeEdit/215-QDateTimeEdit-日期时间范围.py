'''
215-QDateTimeEdit-日期时间范围

API:
    日期时间:
        setMaximumDateTime(QDateTime) -- 设置最大日期时间
        maximumDateTime() -> QDateTime -- 获取最大日期时间对象
        clearMaximumDateTime() -- 清除设置的最大日期时间
        setMinimumDateTime(QDateTime) -- 设置最小日期时间
        minimumDateTime() -> QDateTime -- 获取最小日期时间
        clearMinimumDateTime() -- 清除设置的最小日期时间
        setDateTimeRange(min_datetime, max_datetime) -- 设置日期时间范围  (下同)
    日期:
        setMaximumDate(QDate)
        maximumDate() -> QDate
        clearMaximumDate()
        setMinimumDate(QDate)
        minimumDate() -> QDate
        clearMinimumDate()
        setDateRange(min_date, max_date)
    时间:
        setMaximumTime(QTime)
        maximumTime() -> QTime
        clearMaximumTime()
        setMinimumTime(QTime)
        minimumTime() -> QTime
        clearMinimumTime()
        setTimeRange(min_time, max_time)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit
from PyQt5.QtCore import QDateTime


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('215-QDateTimeEdit-日期时间范围')
        self.resize(1000, 500)

        dte = QDateTimeEdit(self)

        '''设置最大最小日期时间'''
        # 设置最大
        dte.setMaximumDateTime(QDateTime(2022, 1, 1, 1, 1))
        # 设置最小
        dte.setMinimumDateTime(QDateTime(2020, 1, 1, 1, 1))

        # 获取
        print('当前最大日期时间:', dte.maximumDateTime())
        print('当前最小日期时间:', dte.minimumDateTime())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
