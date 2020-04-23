'''
275-QCalendarWidget-常规操作

API:
    showToday() -- 展示今天日期(展示在控件中, 而不是打印出来, 下同)
    showSelectedDate() -- 展示选中的日期
    showNextYear() -- 展示下一年的日期
    showPreviousYear() -- 展示上一年的日期
    showNextMonth() -- 展示下一月的日期
    showPreviousMonth() -- 展示上一月的日期
    setCurrentPage(int year, int month) -- 控制当前界面展示某年某月
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('275-QCalendarWidget-常规操作')
        self.resize(1000, 500)

        cw = QCalendarWidget(self)

        '''控制当前界面展示某年某月'''
        cw.setCurrentPage(2020, 7)

        '''展示今日日期'''
        # cw.showToday()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
