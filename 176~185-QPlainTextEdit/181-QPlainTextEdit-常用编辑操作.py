'''
181-QPlainTextEdit-常用编辑操作
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('181-QPlainTextEdit-常用编辑操作')
        self.resize(1000, 500)

        QPlainTextEdit(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
