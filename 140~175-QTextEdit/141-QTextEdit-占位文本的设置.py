'''
141-QTextEdit-占位文本的设置

API:
    setPlaceholderText(str) -- 设置提示文本
    placeholderText() -> str -- 获取提示文本
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('141-QTextEdit-占位文本的设置')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        '''设置提示文本'''
        te.setPlaceholderText('这是文本提示')

        '''获取提示文本'''
        print(te.placeholderText())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
