'''
160-QTextEdit-文本内容-文本光标-开始和结束编辑块

用户操作文本会根据用户的输入分成多个编辑块, 这些编辑块是系统自动分割的, 例如一个回车是一个编辑块;输入一个单词是一个编辑块.

代码上的对文本的操作是一个统一的编辑块, 可以手动指定编辑块的开始和结束来分割编辑块.

API:
    beginEditBlock() -- 开始编辑块
    endEditBlock() -- 结束编辑块
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('160-QTextEdit-文本内容-文本光标-开始和结束编辑块')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        te_cursor = te.textCursor()

        te_cursor.insertText('123')
        te_cursor.insertText('456')
        te_cursor.insertText('789')

        '''编辑块'''
        te_cursor.beginEditBlock()
        te_cursor.insertText('123')
        te_cursor.endEditBlock()
        te_cursor.beginEditBlock()
        te_cursor.insertText('456')
        te_cursor.endEditBlock()
        te_cursor.beginEditBlock()
        te_cursor.insertText('789')
        te_cursor.endEditBlock()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
