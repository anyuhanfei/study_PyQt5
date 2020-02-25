'''
047_QWidget_鼠标操作_鼠标跟踪案例

创建一个窗口，内部有一个 label 控件
    鼠标移动窗口时，让 label 位置跟随鼠标位置
    让鼠标设置为指定图标
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QCursor


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('047_QWidget_鼠标操作_鼠标跟踪案例')
        self.resize(700, 700)
        self.move(200, 200)

        # 设置鼠标形状
        pixmap = QPixmap('./xxx.png')
        pixmap = pixmap.scaled(30, 30)
        cursor = QCursor(pixmap)
        self.setCursor(cursor)

        # 开启跟踪
        self.setMouseTracking(True)

        # 创建一个 label 控件
        self.label = QLabel(self)
        self.label.setText('hello')

    def mouseMoveEvent(self, mme):
        '''label 控件跟随鼠标移动'''
        self.label.move(mme.localPos().x(), mme.localPos().y())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
