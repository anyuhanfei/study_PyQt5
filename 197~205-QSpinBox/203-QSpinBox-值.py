'''
203-QSpinBox-值

API:
    setValue(int) -- 设置值
    value() -> int -- 获取值
    cleanText() -> str -- 获取值
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('203-QSpinBox-值')
        self.resize(1000, 500)

        sb = QSpinBox(self)

        '''设置值'''
        sb.setValue(180)

        '''获取值'''
        print('当前值:', sb.value())

        sb.setSuffix('aa')
        print('当前值:', sb.text())
        print('当前值:', sb.cleanText())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
