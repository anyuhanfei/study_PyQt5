'''
087_QAbstractButton_点击生效

当点击按钮时，会先执行 hitButton() 方法，当 hitButton() 方法返回 True，那么才是真正的成功点击了。

如果重新 hitButton() 方法，那么可以在此方法内完成一些限定功能。
'''

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Btn(QPushButton):
    def hitButton(self, point):
        '''点击按钮的前置执行函数
        Arge:
            point: 鼠标点击的位置对象，以按钮为左上角为原点的坐标对象
        return:
            bool
        '''
        print(point)
        return True


class Window(QWidget):
    height = 20

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('087_QAbstractButton_点击生效')
        self.resize(500, 500)

        btn = Btn(self)
        btn.move(10, 10)
        btn.setText('btn')
        btn.pressed.connect(lambda: print('点击了按钮'))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
