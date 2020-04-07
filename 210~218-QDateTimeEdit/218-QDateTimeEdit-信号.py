'''
218-QDateTimeEdit-信号

API:
    dateTimeChanged(QDateTime datetime) -- 日期时间改变
    dateChanged(QDate date) -- 日期改变
    timeChanged(QTime time) -- 时间改变
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('218-QDateTimeEdit-信号')
        self.resize(1000, 500)

        dte = QDateTimeEdit(self)

        dte.dateTimeChanged.connect(lambda obj: print('日期时间改变了,', obj))
        dte.dateChanged.connect(lambda obj: print('日期改变了,', obj))
        dte.timeChanged.connect(lambda obj: print('时间改变了,', obj))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
