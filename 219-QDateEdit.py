'''
219-QDateEdit

基于 QDateTimeEdit 控件的小控件
主要操作日期部分

继承自 QDateTimeEdit

没有太多的额外功能, 父类中所有关于操作日期部分的 API, 在这个控件中都是可以使用的.

构造函数:
    QDateEdit(QWidget *parent = nullptr)
    QDateEdit(const QDate &date, QWidget *parent = nullptr)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('219-QDateEdit')
        self.resize(1000, 500)

        QDateEdit(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
