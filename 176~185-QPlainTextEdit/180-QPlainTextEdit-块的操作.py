'''
180-QPlainTextEdit-块的操作

设置用户能够输入的最大块数

若超出了最大块个数时, 又新增一个, 会将第一行删除;
超出最大块的块是被删除了, 而不是隐藏;

API:
    blockCount() -> int -- 当前块个数
    maximumBlockCount() -> int -- 最大块个数
    setMaximumBlockCount(int) -- 设置最大块个数
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPlainTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('180-QPlainTextEdit-块的操作')
        self.resize(1000, 500)

        pte = QPlainTextEdit(self)
        pte.appendPlainText('1\n2\n3\n1\n2\n3\n1\n2\n3\n1\n2\n3\n')

        '''设置最大块个数'''
        pte.setMaximumBlockCount(5)

        '''获取'''
        # 当前块个数
        print('当前块个数:', pte.blockCount())
        # 当前最大块个数
        print('当前最大块个数:', pte.maximumBlockCount())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
