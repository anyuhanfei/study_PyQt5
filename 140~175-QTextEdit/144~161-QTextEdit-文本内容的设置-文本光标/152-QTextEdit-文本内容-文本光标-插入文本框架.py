'''
152-QTextEdit-文本内容-文本光标-插入文本框架

QTextEdit 控件创建后,展示出来的输入框就算是一个文本框架, 在文本框架中可以有多个文本块(段落), 也可以添加子文本框架, 在子文本框架中也可以由文本块.

API:
    insertFrame(QTextFrameFormat) -> QTextFrame
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextFrameFormat


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('152-QTextEdit-文本内容-文本光标-插入文本框架')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        te_cursor = te.textCursor()

        '''插入文本框架'''
        # 创建文本框架的样式
        tff = QTextFrameFormat()
        tff.setBorder(10)
        # 文本框架
        te_cursor.insertFrame(tff)

        '''通过元框架创建新的子文本框架'''
        # 文本文档
        te_document = te.document()
        # 元框架对象
        root_frame = te_document.rootFrame()
        # 设置新的子文本框架
        tff.setBorder(20)
        root_frame.setFrameFormat(tff)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
