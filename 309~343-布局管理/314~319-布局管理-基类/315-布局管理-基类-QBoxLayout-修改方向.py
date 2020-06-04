'''
315-布局管理-基类-QBoxLayout-修改方向

修改方向
    setDirection(QBoxLayout_Direction)
    direction(self) -> QBoxLayout.Direction

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QBoxLayout
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('315-布局管理-基类-QBoxLayout-修改方向')
        self.resize(1000, 500)

        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color: cyan;')
        label2.setStyleSheet('background-color: red;')
        label3.setStyleSheet('background-color: yellow;')

        self.layout = QBoxLayout(QBoxLayout.BottomToTop)
        self.layout.addWidget(label1)
        self.layout.addWidget(label2)
        self.layout.addWidget(label3)

        self.setLayout(self.layout)

        '''定时修改方向'''
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.layout.setDirection((self.layout.direction() + 1) % 4))
        timer.start(1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
