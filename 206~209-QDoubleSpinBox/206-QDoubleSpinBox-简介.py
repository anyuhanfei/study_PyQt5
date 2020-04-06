'''
206-QDoubleSpinBox-简介

浮点类型步长调节器, 如0.00 - 99.99
既可以通过步长调节器调整数据, 也可以通过文本框直接编辑

继承自 QAbstractSpinBox

默认步长为 1.0, 默认范围是 0.00 ~ 99.99
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDoubleSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('206-QDoubleSpinBox-简介')
        self.resize(1000, 500)

        QDoubleSpinBox(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
