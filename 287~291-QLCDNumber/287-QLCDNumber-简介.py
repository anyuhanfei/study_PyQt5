'''
287-QLCDNumber-简介

展示LCD样式的数字
它可以显示几乎任何大小的数字
它可以显示十进制，十六进制，八进制或二进制数

能够展示的字符:
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    A, B, C, D, E, F, h, H, L, o, O, P, r, u, U, Y, g, S
    : ' 空格

继承自QFrame

构造函数:
    QLCDNumber(parent: QWidget = None)
    QLCDNumber(int, parent: QWidget = None)  -- 参数1代表展示的数值位数

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('287-QLCDNumber-简介')
        self.resize(1000, 500)

        lcdn = QLCDNumber(self)
        lcdn.move(10, 10)
        lcdn.display(77)

        lcdn = QLCDNumber(4, self)
        lcdn.move(100, 10)
        lcdn.display(66666)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
