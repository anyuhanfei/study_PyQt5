'''
165-QTextEdit-光标设置

可以修改光标宽度, 若光标宽度增加到一个字符的宽度, 那么这个光标像是要覆盖字符一样, 这个光标样式一般和覆盖模式配合使用, 用来表明开启了覆盖模式.

API:
    setCursorWidth(int) -- 设置光标宽度
    cursorWidth() -- 获取光标宽度
    cursorRect() -> QRect -- 光标矩形
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('165-QTextEdit-光标设置')
        self.resize(1000, 500)

        te = QTextEdit(self)

        '''设置光标宽度'''
        te.setCursorWidth(6)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
