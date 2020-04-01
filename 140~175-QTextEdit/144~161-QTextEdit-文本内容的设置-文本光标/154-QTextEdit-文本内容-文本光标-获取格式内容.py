'''
154-QTextEdit-文本内容-文本光标-获取格式内容

API:
    block() -> QTextBlock -- 获取光标所在的文本块
    blockFormat() -> QTextBlockFormat -- 获取光标所在的文本块格式
    blockCharFormat() -> QTextCharFormat -- 获取光标所在的文本块字符格式
    blockNumber() -> int -- 获取光标所在的文本块编号
    charFormat() -> QTextCharFormat -- 获取文本字符格式
    currentFrame() -> QTextFrame -- 获取当前所在的框架
    currentList() -> QTextList -- 获取当前所在的文本列表
    currentTable() -> QTextTable -- 获取当前的表格
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('154-QTextEdit-文本内容-文本光标-获取格式内容')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)
        te.setText('xxx')

        te_cursor = te.textCursor()

        '''获取光标所在的文本块'''
        print(te_cursor.block())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
