'''
197-QSpinBox-简介

主要处理整数和离散值集, 如:1--99, 1月--12月, 周一--周日
允许用户通过单击向上/向下按钮或按键盘上的上/下来选择一个值来增加/减少当前显示的值。用户还可以手动键入值
旋转框支持整数值
也可以子类化此类实现更多支持

继承自 QAbstractSpinBox.


'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('197-QSpinBox-简介')
        self.resize(1000, 500)

        QSpinBox(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
