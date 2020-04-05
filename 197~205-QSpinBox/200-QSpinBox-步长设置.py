'''
200-QSpinBox-步长设置

设置步长调节器, 单步步长值

API:
    setSingleStep(step_int) -- 设置步长
    singleStep() -> int -- 获取步长
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('200-QSpinBox-步长设置')
        self.resize(1000, 500)

        sb = QSpinBox(self)

        '''设置步长'''
        sb.setSingleStep(2)

        '''获取步长'''
        print('当前步长:', sb.singleStep())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
