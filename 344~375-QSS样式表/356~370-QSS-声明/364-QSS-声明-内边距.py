'''
364-QSS-声明-内边距

统一设置 -- padding: 上 右 下 左
分开设置 -- padding-top
            padding-right
            padding-bottom
            padding-left
常用取值:
    16px
    1em

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('364-QSS-声明-内边距')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
