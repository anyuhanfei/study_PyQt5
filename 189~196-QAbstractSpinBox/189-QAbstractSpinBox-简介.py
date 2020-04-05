'''
189-QAbstractSpinBox-简介

步长调节器, 它是一个组合控件, 在左侧有一个输入文本框, 旁边有两个箭头按钮, 如果按下箭头按钮, 那么就会修改输入文本框中的内容(按一定规律).

其中 QSpinBox 整型数字步长调节器, QDoubleSpinBox 浮点型数字步长调节器, QDateTimeEdit 时间日期调节器 都是这一类型的控件. 它们都是继承自 QAbstractSpinBox.

继承自 QWidget.

直接使用有样式, 但是步长调节功能
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QAbstractSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('189-QAbstractSpinBox-简介')
        self.resize(1000, 500)

        asb = QAbstractSpinBox(self)
        asb.resize(100, 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
