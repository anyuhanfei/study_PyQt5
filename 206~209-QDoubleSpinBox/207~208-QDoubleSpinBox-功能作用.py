'''
207~208-QDoubleSpinBox-功能作用

QDoubleSpinBox 大部分功能和 QSpinBox 类似, 仅有关于小数部分的功能是独立的.

API:
    setDecimals(int) -- 设置小数位数
    decimals() -> int -- 获取小数位数
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QDoubleSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('207~208-QDoubleSpinBox-功能作用')
        self.resize(1000, 500)

        dsb = QDoubleSpinBox(self)

        '''设置小数位数'''
        dsb.setDecimals(4)

        '''获取小数位数'''
        print('小数位数:', dsb.decimals())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
