'''
199-QSpinBox-数值循环

设置数值达到最大/小时, 跳转到最小/大

API:
    setWrapping(bool) -- 设置是否是数值循环
    wrapping() -> bool -- 获取是否是数值循环

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('199-QSpinBox-数值循环')
        self.resize(1000, 500)

        sb = QSpinBox(self)

        '''设置是否是数值循环'''
        sb.setWrapping(True)

        '''获取是否是数值循环'''
        print('获取是否是数值循环:', sb.wrapping())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
