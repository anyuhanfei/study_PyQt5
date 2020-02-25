'''
055_QWidget_层级关系
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('055_QWidget_层级关系')
        self.resize(500, 500)
        self.move(200, 200)

        label_1 = QLabel(self)
        label_1.move(10, 10)
        label_1.resize(100, 100)
        label_1.setStyleSheet('background-color: red;')

        label_2 = QLabel(self)
        label_2.move(10, 80)
        label_2.resize(100, 100)
        label_2.setStyleSheet('background-color: greed;')

        label_3 = QLabel(self)
        label_3.move(60, 40)
        label_3.resize(100, 100)
        label_3.setStyleSheet('background-color: yellow;')

        '''默认情况下，重叠控件按照创建的时间，创建越晚层级越高'''

        # 将 label_2 放在最底层
        label_2.lower()

        # 将 label_1 放在最高层
        label_1.raise_()

        # 将 label_3 放在 label_2 下
        label_3.stackUnder(label_2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
