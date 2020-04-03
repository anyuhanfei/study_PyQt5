'''
169-QTextEdit-当前字符格式

API:
    setCurrentCharFormat(QTextCharFormat) -- 设置当前字符格式
    mergeCurrentCharFormat(QTextCharFormat) -- 
    currentCharFormat() -> QTextCharFormat -- 

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.QtGui import QTextCharFormat


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('169-QTextEdit-当前字符格式')
        self.resize(1000, 500)

        te = QTextEdit(self)

        # 字符格式
        tcf = QTextCharFormat()
        tcf.setFontWeight(20)
        tcf.setFontPointSize(20)
        # 设置字符格式
        te.setCurrentCharFormat(tcf)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
