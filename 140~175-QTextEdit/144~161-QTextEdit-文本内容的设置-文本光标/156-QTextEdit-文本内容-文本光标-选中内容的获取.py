'''
156-QTextEdit-文本内容-文本光标-选中内容的获取

API:
    selectedText() -> str -- 获取选中的文本
    selection() -> QTextDocumentFragment -- 获取选中的文本文档对象
    selectedTableCells() -> (int firstRow, int numRows, int firstColumn, int numColumns) -- 获取选中的表格
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextCursor


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('156-QTextEdit-文本内容-文本光标-选中内容的获取')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)
        te.setText('abcdefghijklmn')

        te_cursor = te.textCursor()

        # 设置一些选中的文本
        te_cursor.setPosition(10, QTextCursor.KeepAnchor)
        te.setTextCursor(te_cursor)

        '''获取选中的文本'''
        print('获取选中的文本:', te_cursor.selectedText())

        '''获取选中文本的对象'''
        print('获取选中文本的对象:', te_cursor.selection().toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
