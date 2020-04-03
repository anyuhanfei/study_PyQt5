'''
175-QTextEdit-信号的使用

API:
    textChanged() -- 文本内容发生改变时, 发射的信号
    selectionChanged() -- 选中内容发生改变时, 发射的信号
    cursorPositionChanged() -- 光标位置发生改变时, 发射的信号
    currentCharFormatChanged(QTextCharFormat) -- 当前额字符格式发生改变时, 发射的信号
    copyAvailable(bool yes) -- 复制可用时
    redoAvailable(bool available) -- 重做可用时
    undoAvailable(bool available) -- 撤销可用时
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('175-QTextEdit-信号的使用')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
