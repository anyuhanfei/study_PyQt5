'''
159-QTextEdit-文本内容-文本光标-位置判断获取

API:
    atBlockEnd() -- 是否在文本块末尾
    atBlockStart() -- 是否在文本块开始
    atEnd() -- 是否在文档末尾
    atStart() -- 是否在文档开始
    columnNumber() -> int -- 在第几列
    position() -- 光标位置
    positionInBlock() -- 在文本块中的位置
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)
        te.setText('1234567')

        te_cursor = te.textCursor()

        '''位置相关'''
        print('是否在文本块末尾:', te_cursor.atBlockEnd())
        print('是否在文本块开始:', te_cursor.atBlockStart())
        print('是否在文档末尾:', te_cursor.atEnd())
        print('是否在文档开始:', te_cursor.atStart())
        print('在第几列:', te_cursor.columnNumber())
        print('光标位置:', te_cursor.position())
        print('positionInBlock:', te_cursor.positionInBlock())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
