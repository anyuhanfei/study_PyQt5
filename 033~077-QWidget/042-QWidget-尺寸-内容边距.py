'''
042-QWidget-尺寸-内容边距
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('042_QWidget_尺寸_内容边距')
        self.resize(700, 700)
        self.move(500, 500)

        label = QLabel(self)
        label.resize(300, 300)
        label.move(100, 100)
        label.setStyleSheet("background-color: red;")
        label.setText('hello')

        # 获取内容区域，返回值是一个类似元组的对象
        print(label.contentsRect())

        # 设置内容边距
        label.setContentsMargins(0, 0, 200, 200)

        # 获取内容边距，返回值是一个元组
        print(label.getContentsMargins())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
