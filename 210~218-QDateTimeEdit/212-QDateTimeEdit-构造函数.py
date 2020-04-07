'''
212-QDateTimeEdit-构造函数

根据指定日期或时间, 创建出日期时间编辑器控件
并会初始化该控件展示的section

可以只传一个父类, 也可以事先创建好时间对象, 传入 QDateTimeEdit 控件中.

API:
    QDateTimeEdit(parent: QWidget = None)
    QDateTimeEdit(Union[QDateTime, datetime.datetime], parent: QWidget = None)
    QDateTimeEdit(Union[QDate, datetime.date], parent: QWidget = None)
    QDateTimeEdit(Union[QTime, datetime.time], parent: QWidget = None)

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit
from PyQt5.QtCore import QDateTime


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('212-QDateTimeEdit-构造函数')
        self.resize(1000, 500)

        # 方法一
        dte = QDateTimeEdit(self)
        dte.move(10, 10)

        # 方法二
        dt = QDateTime(2020, 1, 1, 1, 1)
        dte = QDateTimeEdit(dt, self)
        dte.move(10, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
