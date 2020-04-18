'''
274-QCalendarWidget-日期选中

API:
    setSelectedDate(QDate date) -- 设置选中日期
    setSelectionMode(QCalendarWidget.SelectionMode mode) -- 设置模式
    selectionMode() -> QCalendarWidget.SelectionMode -- 获取模式

附:
    QCalendarWidget.SelectionMode
        QCalendarWidget.NoSelection -- 日期无法选择
        QCalendarWidget.SingleSelection -- 可以选择单日期
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('274-QCalendarWidget-日期选中')
        self.resize(1000, 500)

        cw = QCalendarWidget(self)
        '''设置模式'''
        cw.setSelectionMode(QCalendarWidget.NoSelection)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
