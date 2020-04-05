'''
182-QPlainTextEdit-滚动内容以显示光标

API:
    centerCursor() -- 控制光标, 尽可能保证光标在文本框中间
    ensureCursorVisible() -- 滚动控件, 确保光标可见
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('182-QPlainTextEdit-滚动内容以显示光标')
        self.resize(1000, 500)

        pte = QPlainTextEdit(self)
        pte.resize(100, 100)
        pte.setPlainText('1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1\n')

        '''控制光标'''
        pte.centerCursor()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
