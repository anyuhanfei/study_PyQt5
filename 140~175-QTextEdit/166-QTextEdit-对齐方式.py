'''
166-QTextEdit-对齐方式

API:
    setAlignment(Qt.Alignment) -- 设置对齐方式
    alignment() -> Qt.Alignment -- 获取对齐方式

Qt.Alignment
    Qt.AlignLeft -- 向左
    Qt.AlignRight -- 向右
    Qt.AlignCenter -- 居中
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('166-QTextEdit-对齐方式')
        self.resize(1000, 500)

        te = QTextEdit(self)

        '''设置对齐方式'''
        te.setAlignment(Qt.AlignCenter)

        '''获取对齐方式'''
        print('当前对齐方式:', te.alignment())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
