'''
086_QAbstractButton_模拟点击

使用代码来模拟按钮点击，一般是用来执行按钮点击信号绑定的槽函数

API:
    click() -- 普通点击
    animateClick(ms) -- 动画点击
'''

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel


class Window(QWidget):
    height = 20

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('086_QAbstractButton_模拟点击')
        self.resize(500, 500)

        self.btn_one = QPushButton(self)
        self.btn_one.setText('btn')
        self.btn_one.move(10, 10)
        self.btn_one.pressed.connect(self._btn_pressed)

        '''模拟用户点击'''
        self.btn_one.click()

        '''动画点击'''
        self.btn_one.animateClick(2000)  # 点击的持续时间 单位为毫秒

    def _btn_pressed(self):
        self.height += 30
        self.label = QLabel(self)
        self.label.move(10, self.height)
        self.label.setText('点击了按钮')
        self.label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
