'''
220-QTimeEdit

基于 QDateTimeEdit 控件的小控件
主要操作时间部分

继承自 QDateTimeEdit

没有太多的额外功能, 父类中所有关于操作日期部分的 API, 在这个控件中都是可以使用的.

构造函数:
    QTimeEdit(QWidget *parent = nullptr)
    QTimeEdit(const QTime &time, QWidget *parent = nullptr)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTimeEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('220-QTimeEdit')
        self.resize(1000, 500)

        QTimeEdit(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
