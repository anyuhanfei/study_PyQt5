'''
088_QAbstractButton_可用信号

pressed() -- 鼠标按下信号
released() -- 鼠标释放(控件内松开鼠标 或 鼠标移出控件范围后)
clicked(checked = false) -- 控件内按下+控件内释放
toggled(bool checked) -- 切换信号(一般在单选框或者复选框中使用)
'''

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel


class Window(QWidget):
    height = 20

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('087_QAbstractButton_点击生效')
        self.resize(500, 500)

        self.btn = QPushButton(self)
        self.btn.move(10, 10)
        self.btn.setText('btn')
        self.btn.setCheckable(True)

        '''按下控件时的信号'''
        self.btn.pressed.connect(self._pressed)

        '''释放控件时的信号'''
        self.btn.released.connect(self._released)

        '''控件内按下并释放的信号'''
        self.btn.clicked.connect(self._clicked)

        '''切换选中状态的信号'''
        self.btn.toggled.connect(self._toggled)

    def _pressed(self):
        self.height += 30
        label = QLabel(self)
        label.move(10, self.height)
        label.setText('按下控件')
        label.show()

    def _released(self):
        self.height += 30
        label = QLabel(self)
        label.move(10, self.height)
        label.setText('释放控件')
        label.show()

    def _clicked(self, value):
        self.height += 30
        label = QLabel(self)
        label.move(10, self.height)
        label.setText('点击控件，当前选中状态为 %s' % (value))
        label.show()

    def _toggled(self, value):
        self.height += 30
        label = QLabel(self)
        label.move(10, self.height)
        label.setText('切换了选中状态，当前选中状态为 %s' % (value))
        label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
