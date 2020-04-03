'''
043-QWidget-鼠标操作-形状设置
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('043_QWidget_鼠标操作_形状设置')
        self.resize(700, 700)
        self.move(200, 200)

        # 修改鼠标形状
        self.setCursor(Qt.PointingHandCursor)

        # 重置鼠标形状
        self.unsetCursor()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
