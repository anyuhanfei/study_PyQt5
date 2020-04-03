'''
043-QWidget-鼠标操作-自定义形状
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QCursor


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('043_QWidget_鼠标操作_自定义形状')
        self.resize(700, 700)
        self.move(200, 200)

        '''
        setCursor() 第一个参数接收一个鼠标对象，那么可以先创建一个鼠标对象
        QCursor() 第一个参数接收一个图片对象，那么就先创建一个图片对象
        QPixmap() 创建一个图片对象，需要传入一个图片路径
        '''
        pixmap = QPixmap('./xxx.png')
        pixmap = pixmap.scaled(50, 50)  # 缩放后，回返回一个新对象，需要重新接收
        cursor = QCursor(pixmap, 0, 0)  # 第二个，第三个参数是鼠标有效的坐标，默认在图片正中央
        self.setCursor(cursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
