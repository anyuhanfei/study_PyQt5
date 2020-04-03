'''
137-QFrame-简介

是一个基类, 可以选择直接使用

主要是用来控制一些边框样式, 如凸起、凹下、阴影、线宽

继承自 QWidget

创建 QFrame：QFrame(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())

它的信号全部继承自 QWidget
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFrame


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('137_QFrame_简介')
        self.resize(1000, 500)

        # 创建一个 QFrame 控件
        f = QFrame(self)
        f.resize(100, 100)
        f.move(10, 10)
        f.setStyleSheet('background-color: red;')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
