'''
292-QProgressBar-简介

提供一个水平或垂直进度条
进度条用于向用户提供操作进度的指示，并向他们保证应用程序仍在运行

继承自QWidget

构造函数:
    QProgressBar(self)

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('292-QProgressBar-简介')
        self.resize(1000, 500)

        QProgressBar(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
