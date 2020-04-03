'''
089-QPushButton-构造函数

实例化一个 QPushButton 控件有几种方法，一些方法通过实例化时传参的方式设置了属性，可以节省一行代码：
    QPushButton() -- 创建一个无父控件的按钮控件
    QPushButton(parent) -- 创建控件的同时, 设置父控件
    QPushButton(text, parent) -- 创建控件的同时, 设置提示文本和父控件
    QPushButton(icon, text, parent) -- 创建控件的同时, 设置图标, 提示文本和父控件
'''

import sys


from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('089_QPushButton_构造函数')
        self.resize(500, 500)

        icon = QIcon('./xxx.png')
        text = 'btn'

        '''以下都将实现同样的按钮'''
        # 无参数
        btn_one = QPushButton()
        btn_one.setParent(self)
        btn_one.setIcon(icon)
        btn_one.setText(text)

        # 传入父控件
        btn_two = QPushButton(self)
        btn_two.setIcon(icon)
        btn_two.setText(text)

        # 传入提示文本和父控件
        btn_three = QPushButton(text, self)
        btn_three.setIcon(icon)

        # 传入图标、提示文本和父控件
        btn_four = QPushButton(icon, text, self)

        btn_one.move(10, 10)
        btn_two.move(10, 40)
        btn_three.move(10, 70)
        btn_four.move(10, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
