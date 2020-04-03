'''
168-QTextEdit-字体颜色

API:
    setTextBackgroundColor(QColor) -- 将当前格式的文本背景颜色设置为指定颜色
    textBackgroundColor() -> QColor -- 获取当前文本背景颜色
    setTextColor(QColor) -- 将当前格式的文本颜色设置为指定颜色
    textColor() -> QColor -- 获取当前文本颜色
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.Qt import QColor


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('168-QTextEdit-字体颜色')
        self.resize(1000, 500)

        te = QTextEdit(self)

        '''背景颜色'''
        te.setTextBackgroundColor(QColor(100, 150, 100))

        '''字体颜色'''
        te.setTextColor(QColor(200, 150, 200))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
