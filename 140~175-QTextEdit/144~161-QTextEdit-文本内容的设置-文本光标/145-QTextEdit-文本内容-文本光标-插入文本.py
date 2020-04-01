'''
145-QTextEdit-文本内容-文本光标-插入文本

API:
    insertText(str) -- 插入文本(普通文本)
    insertText(QString text, QTextCharFormat format) -- 插入文本, 带格式 (QTextCharFormat -- 针对于部分字符的格式描述)
    insertHtml(html_str) -- 插入 HTML 字符串
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextCharFormat


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('145-QTextEdit-文本内容-文本光标-插入文本')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        '''文本光标对象'''
        te_cursor = te.textCursor()

        '''插入普通文本'''
        te_cursor.insertText('ccc')

        '''插入带格式的普通文本'''
        # 设置格式对象
        tcf = QTextCharFormat()
        tcf.setFontPointSize(20)
        # 将格式与内容插入到文本中
        te_cursor.insertText('bbb', tcf)

        '''插入 html 格式的文本'''
        te_cursor.insertHtml('<h1>aaa</h1>')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
