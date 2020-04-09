'''
233-QAbstractSlider-简介

提供的范围内的整数值
是一个抽象类

继承自 QWidget
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSlider


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('233-QAbstractSlider-简介')
        self.resize(1000, 500)

        s = QSlider(self)
        s.move(10, 10)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
