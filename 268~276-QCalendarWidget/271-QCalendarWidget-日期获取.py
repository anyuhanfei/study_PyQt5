'''
271-QCalendarWidget-日期获取

monthShown() -> int -- 月
yearShown() -> int -- 年
selectedDate() -> QDate -- 日期对象
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('271-QCalendarWidget-日期获取')
        self.resize(1000, 500)

        cw = QCalendarWidget(self)

        '''获取'''
        print('年:', cw.yearShown())
        print('月:', cw.monthShown())
        print('日期对象:', cw.selectedDate())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
