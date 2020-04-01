'''
153-QTextEdit-文本内容-文本光标-格式操作

一般用于给定的多个样式集, 需要哪个就将光标移动到需要改变的文本块上, 然后点击按钮等可触发控件, 触发方法, 修改文本样式

API:
    setBlockCharFormat(QTextCharFormat) -- 设置要格式化的当前块（或选择中包含的所有块）的块 char 格式
    setBlockFormat(QTextBlockFormat) -- 设置当前块的块格式（或选择中包含的所有块）以进行格式化
    setCharFormat(QTextCharFormat) -- 将光标的当前字符格式设置为给定格式。如果光标有选择，则给定格式应用于当前选择
    mergeBlockCharFormat(QTextCharFormat) -- 合并当前块的 char 格式
    mergeBlockFormat(QTextBlockFormat) -- 合并当前块的格式
    mergeCharFormat(QTextCharFormat) -- 合并当前字符格式
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextCharFormat


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('153-QTextEdit-文本内容-文本光标-格式操作')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        te_cursor = te.textCursor()

        '''格式操作'''
        # 设置一些样式
        tcf = QTextCharFormat()
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        # 设置
        te_cursor.setCharFormat(tcf)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
