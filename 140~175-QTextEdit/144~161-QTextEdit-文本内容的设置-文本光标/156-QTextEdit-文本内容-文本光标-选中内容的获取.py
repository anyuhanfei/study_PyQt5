'''

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.move(10, 10)

        '''文本文档对象'''
        te_obj = te.document()

        # 打印一下文本文档对象
        print(te_obj)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
