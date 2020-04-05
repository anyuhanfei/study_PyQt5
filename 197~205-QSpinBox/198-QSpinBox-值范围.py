'''
198-QSpinBox-值范围

API:
    setMaximum(max_num) -- 设置最大值
    maximum() -> int -- 获取最大值
    setMinimum(min_num) -- 设置最小值
    minimum() -> int -- 获取最小值
    setRange(min_num, max_num) -- 设置数值区间

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('198-QSpinBox-值范围')
        self.resize(1000, 500)

        sb = QSpinBox(self)

        '''最大值'''
        # 设置最大值
        sb.setMaximum(1000)
        # 获取最大值
        print('最大值:', sb.maximum())

        '''最小值'''
        # 设置最小值
        sb.setMinimum(100)
        # 获取最小值
        print('最小值:', sb.minimum())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
