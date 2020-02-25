'''
048_QWidget_事件_事件转发机制
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyLabel(QLabel):
    def mousePressEvent(self, QMouseEvent):
        print('子控件被按下')


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('048_QWidget_事件_事件转发机制')
        self.resize(700, 700)
        self.move(200, 200)

        # 实例化一个自定义的 label 控件，这个控件有定义自己的鼠标按下事件
        child_label_one = MyLabel(self)
        child_label_one.setText('label one')
        child_label_one.move(10, 10)
        # 实例化一个 label 控件，这个控件没有定义鼠标按下事件
        child_label_two = QLabel(self)
        child_label_two.setText('label two')
        child_label_two.move(10, 50)

        # 按下父控件和 label 子控件，会打印 父控件被按下
        # 按下自定义的 label 子控件，会打印 子控件被按下
        # 当子控件没有定义相应的事件时，会转发给父控件的事件

    def mousePressEvent(self, QMouseEvent):
        print('父控件被按下')

        # 忽略本事件的处理（如果有父控件，就会转发给父控件的事件函数）
        QMouseEvent.ignore()

        # 获取事件处理状态
        static = QMouseEvent.isAccepted()
        print(static)

        # 指定本事件已经被处理
        QMouseEvent.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
