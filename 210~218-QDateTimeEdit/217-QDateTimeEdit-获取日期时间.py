'''
217-QDateTimeEdit-获取日期时间

API:
    dateTime() -> QDateTime
    date() -> QDate
    time() -> QTime
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('217-QDateTimeEdit-获取日期时间')
        self.resize(1000, 500)

        self.dte = QDateTimeEdit(self)

        btn = QPushButton('获取日期时间', self)
        btn.move(00, 50)
        btn.clicked.connect(lambda: print('获取到的日期时间:', self.dte.dateTime()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
