'''
341-布局管理-QStackedLayout-信号

currentChanged(int index) -- 当前展示的控件发生变化时
widgetRemoved(int index) -- 控件移除时

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QStackedLayout
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('341-布局管理-QStackedLayout-信号')
        self.resize(1000, 500)

        self.sl = QStackedLayout()
        self.setLayout(self.sl)

        label_1 = QLabel('aaa')
        label_2 = QLabel('bbb')
        label_1.setStyleSheet('background-color: red;')
        label_2.setStyleSheet('background-color: blue;')

        self.sl.addWidget(label_1)
        self.sl.addWidget(label_2)

        self.i = 0

        def text():
            self.sl.setCurrentIndex(self.i)
            self.i = (self.i + 1) % 2

        timer = QTimer(self)
        timer.timeout.connect(text)
        timer.start(1000)

        self.sl.currentChanged.connect(lambda: print('改变了'))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
