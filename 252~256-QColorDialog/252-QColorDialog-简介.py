'''
252-QColorDialog-简介

颜色对话框的功能是允许用户选择颜色

继承自 QDialog
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('252-QColorDialog-简介')
        self.resize(1000, 500)

        cd = QColorDialog(self)

        cd.open()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
