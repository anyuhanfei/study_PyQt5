'''
248-QFontDialog-简介

提供了一种选择字体的对话框控件

继承自 QDialog
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFontDialog


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('248-QFontDialog-简介')
        self.resize(1000, 500)

        fd = QFontDialog(self)
        fd.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
