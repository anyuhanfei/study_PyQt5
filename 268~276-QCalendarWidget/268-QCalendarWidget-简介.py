'''
268-QCalendarWidget-简介

提供了一个基于每月日历控件，允许用户选择一个日期

继承自 QWidget

构造函数:
    QCalendarWidget(parent: QWidget = None)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('268-QCalendarWidget-简介')
        self.resize(1000, 500)

        QCalendarWidget(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
