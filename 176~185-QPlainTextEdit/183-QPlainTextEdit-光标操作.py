'''
183-QPlainTextEdit-光标操作

API:
    textCursor() -> QTextCursor -- 获取文本光标对象
    cursorForPosition(QPoint) -> QTextCursor -- 获取指定位置的文本光标对象
    cursorWidth() -> int -- 获取文本光标宽度
    setCursorWidth(int) -- 设置文本光标宽度
    cursorRect() -> QRect -- 获取文本光标矩形
    cursorRect(QTextCursor) -- 获取指定光标对象的矩形
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('183-QPlainTextEdit-光标操作')
        self.resize(1000, 500)

        pte = QPlainTextEdit(self)

        '''获取文本光标对象'''
        print(pte.textCursor())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
