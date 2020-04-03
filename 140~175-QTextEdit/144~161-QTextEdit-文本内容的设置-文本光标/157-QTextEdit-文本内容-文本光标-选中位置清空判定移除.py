'''
157-QTextEdit-文本内容-文本光标-选中位置获清空判定移除

API:
    selectionStart() -> int -- 选中文本的起始位置
    selectionEnd() -> int -- 选中文本的结束位置

    clearSelection() -- 取消文本的选中(需要反向设定)
    hasSelection() -> bool -- 是否有选中文本

    removeSelectedText() -- 移除选中的文本
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextCursor


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)
        te.setText('abcde\nfghijklmn')

        te_cursor = te.textCursor()

        # 先选中一些文本
        te_cursor.setPosition(10, QTextCursor.KeepAnchor)
        te.setTextCursor(te_cursor)

        '''位置'''
        print('选中文本的起始位置:', te_cursor.selectionStart())
        print('选中文本的结束位置:', te_cursor.selectionEnd())

        '''取消选中'''
        te_cursor.clearSelection()
        te.setTextCursor(te_cursor)

        '''是否有选中的文本'''
        print('是否有选中的文本:', te_cursor.hasSelection())

        '''删除选中文本'''
        te_cursor.setPosition(2, QTextCursor.KeepAnchor)
        te.setTextCursor(te_cursor)
        te_cursor.removeSelectedText()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
