'''
177-QPlainTextEdit-占位文本_只读_字符格式

API:
    setPlaceholderText(str) -- 设置占位文本
    placeholderText() -> str -- 获取占位文本

    setReadOnly(bool) -- 设置是否是只读
    isReadOnly() -> bool -- 获取是否是只读

    currentCharFormat() -> QTextCharFormat -- 获取当前的字符格式
    setCurrentCharFormat(QTextCharFormat) -- 设置字符格式
    mergeCurrentCharFormat(QTextCharFormat) -- 合并字符格式
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit
from PyQt5.QtGui import QTextCharFormat


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('177-QPlainTextEdit-占位文本_只读_字符格式')
        self.resize(1000, 500)

        pte = QPlainTextEdit(self)

        '''占位文本'''
        # 设置占位文本
        pte.setPlaceholderText('这是占位符')
        # 获取占位文本
        print('获取占位文本:', pte.placeholderText())

        '''只读'''
        # 设置为只读
        pte.setReadOnly(True)
        # 获取是否是只读
        print('获取是否是只读:', pte.isReadOnly())

        '''字符格式'''
        tcf = QTextCharFormat()
        tcf.setFontUnderline(True)
        pte.setCurrentCharFormat(tcf)
        pte.setPlainText('123')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
