'''
320-布局管理-QHBoxLayout-QVBoxLayout

QHBoxLayout 和 QVBoxLayout 在功能上与父类没有什么太大的区别和新添加的功能, 仅仅是确认了排列的方向而已

使用 setDirection() 方法还可以修改方向
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('320-布局管理-QHBoxLayout-QVBoxLayout')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
