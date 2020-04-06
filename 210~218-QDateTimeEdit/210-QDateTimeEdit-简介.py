'''
210-QDateTimeEdit-简介

日期时间编辑器

编辑日期和时间的单行文本框
既可以用箭头调节, 也可以用键盘编辑输入
可以单独调节某个部分

继承自 QAbstractSpinBox

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('210-QDateTimeEdit-简介')
        self.resize(1000, 500)

        QDateTimeEdit(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
