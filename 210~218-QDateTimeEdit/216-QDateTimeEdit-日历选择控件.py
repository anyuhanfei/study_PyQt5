'''
216-QDateTimeEdit-日历选择控件

通过日历选择控件, 快速的让用户输入日期

API:
    setCalendarPopup(bool) -- 设置是否弹出日历选择控件
    calendarPopup() -- 获取是否弹出日历选择控件
    setCalendarWidget(QCalendarWidget) -- 设置自定义日历选择控件
    calendarWidget() -> QCalendarWidget -- 获取自定义日历选择控件

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('216-QDateTimeEdit-日历选择控件')
        self.resize(1000, 500)

        dte = QDateTimeEdit(self)

        '''弹出日历选择控件'''
        # 设置
        dte.setCalendarPopup(True)
        # 获取
        print('获取是否弹出日历选择控件:', dte.calendarPopup())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
