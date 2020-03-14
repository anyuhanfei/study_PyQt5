'''
092_QPushButton_默认处理

在有多个按钮并且必须要点击一个的时候（通常是对话框），设置一个默认按钮，可以让使用者按回车键快速点击。

API
    setAutoDefault(bool) -- 点击按钮后设置成默认按钮
    setDefault(bool) -- 直接设置成默认按钮
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel


class Window(QWidget):
    widget = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('092_QPushButton_默认处理')
        self.resize(1000, 500)

        btn_one = QPushButton('btn_one', self)
        btn_one.move(10, 10)

        btn_two = QPushButton('btn_two', self)
        btn_two.move(100, 10)

        '''设置自动默认'''
        btn_one.setAutoDefault(True)

        '''设置默认'''
        btn_two.setDefault(True)

        '''获取按钮是否是自动默认'''
        btn_one_is_auto_default = btn_one.autoDefault()
        btn_two_is_auto_default = btn_two.autoDefault()

        '''获取按钮是否是默认'''
        btn_one_is_default = btn_one.isDefault()
        btn_two_is_default = btn_two.isDefault()

        label = QLabel('btn_one 是否是自动默认：%s' % (btn_one_is_auto_default), self)
        label.move(10, 40)

        label = QLabel('btn_two 是否是自动默认：%s' % (btn_two_is_auto_default), self)
        label.move(10, 70)

        label = QLabel('btn_one 初始化时是否是默认的：%s' % (btn_one_is_default), self)
        label.move(10, 100)

        label = QLabel('btn_two 初始化时是否是默认的：%s' % (btn_two_is_default), self)
        label.move(10, 130)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
