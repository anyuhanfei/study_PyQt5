'''
045-QWidget-鼠标操作-鼠标对象
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QCursor


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('045_QWidget_鼠标操作_鼠标对象')
        self.resize(700, 700)
        self.move(200, 200)

        pixmap = QPixmap('./xxx.png')
        pixmap = pixmap.scaled(50, 50)
        cursor = QCursor(pixmap, 0, 0)  # 这是鼠标对象，在鼠标对象中有很多其他功能
        self.setCursor(cursor)

        # 获取当前鼠标的位置，桌面坐标系
        print(cursor.pos())

        # 设置当前鼠标的位置(打开时会将鼠标移动至指定坐标上)
        cursor.setPos(100, 100)

        # 以上是自定义鼠标，会通过 QCursor() 函数创建一个鼠标对象，若不设置或使用系统自带的鼠标形状，那么将不需要创建鼠标对象，其实在控件中就已经有鼠标对象了
        print(self.cursor())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
