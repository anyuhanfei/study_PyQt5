'''
363-QSS-声明-外边距

统一设置 -- margin: 上 右 下 左
分开设置 -- margin-top
            margin-right
            margin-bottom
            margin-left
常用取值:
    16px
    1em

注意: resize 调整的是包含外边距的尺寸, 外边距变大, 边框以内尺寸会变小

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('363-QSS-声明-外边距')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
