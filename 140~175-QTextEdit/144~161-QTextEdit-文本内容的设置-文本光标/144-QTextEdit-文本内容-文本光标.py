'''
144~161-QTextEdit-文本内容的设置-文本光标

文本编辑器本质是给用户一个可视化的输入框, 然后用户可以通过这个可视化的输入框进行操作文本文档.
文本文档是一个对象, 这个对象存储文本内容.
前文中学习的文本内容设置的一些API也是直接在可视化的输入框进行操作.
而文本文本光标可以直接操作文本文档, 然后再在可视化的输入框中展示操作后的文本.

API:
    te.document() -> QTextDocument -- 获取文本文档的方法

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('144~161-QTextEdit-文本内容的设置-文本光标')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        '''文本文档对象'''
        te_obj = te.document()

        # 打印一下文本文档对象
        print(te_obj)

        '''文本光标'''
        te_cursor = te.textCursor()

        # 打印一下文本光标对象
        print(te_cursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
