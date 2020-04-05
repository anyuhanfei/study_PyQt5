'''
204-QSpinBox-自定义展示格式

展示数值之前, 调用此方法, 转换成对应的格式字符串进行展示

方法重写:
    textFromValue(self, p_int) -> format_str
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox


class MyQSpinBox(QSpinBox):
    def textFromValue(self, int):
        return '数字(%s)' % (int)


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('204-QSpinBox-自定义展示格式')
        self.resize(1000, 500)

        MyQSpinBox(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
