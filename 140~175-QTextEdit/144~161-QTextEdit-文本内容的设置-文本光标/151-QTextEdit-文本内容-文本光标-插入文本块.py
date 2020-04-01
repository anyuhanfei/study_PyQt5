'''
151-QTextEdit-文本内容-文本光标-插入文本块

文本块其实就是一段文本

API:
    insertBlock() -- 插入一个空的文本块
    insertBlock(QTextBlockFormat) -- 插入文本块的同时, 设置文本块格式
    insertBlock(QTextBlockFormat, QTextCharFormat) -- 插入文本块的同时, 设置文本块格式和文本字符格式
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextBlockFormat, QTextCharFormat


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('151-QTextEdit-文本内容-文本光标-插入文本块')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        te_cursor = te.textCursor()

        '''插入文本块'''
        # 普通
        te_cursor.insertBlock()

        # 有文本块格式
        tbf = QTextBlockFormat()
        tbf.setIndent(3)
        te_cursor.insertBlock(tbf)

        # 有文本块格式和文本字符格式
        tcf = QTextCharFormat()
        tcf.setFontPointSize(20)
        te_cursor.insertBlock(tbf, tcf)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
