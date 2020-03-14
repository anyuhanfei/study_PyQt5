'''
082_QAbstractButton_快捷键设置

通过指定的快捷键，触发按钮的点击

快捷键的触发有多种情况：
    当没有进行任何的快捷键设置时，被选中的按钮(有焦点的按钮)可以通过空格键触发点击；
    按钮的文本设置有 '&' 符号时，'&' 符号不会被显示，并且 'Alt'键 + '&' 符号后的符号就是自动创建的快捷键；
    setShortcut() 方法设置按钮快捷键；
'''

import sys


from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('082_QAbstractButton_快捷键设置')
        self.resize(500, 500)

        # self.实验空格快捷键()

        '''& 符号的快捷键'''
        self.btn_four = QPushButton(self)
        self.btn_four.clicked.connect(lambda: print('btn_four 被点击'))
        self.btn_four.setText('this a butt&on')  # 快捷键是 alt+o
        self.btn_four.move(200, 10)

        '''setShortcut() 设置快捷键'''
        self.btn_five = QPushButton(self)
        self.btn_five.setText('test setShortcut()')
        self.btn_five.move(200, 60)
        self.btn_five.clicked.connect(lambda: print('btn_five 被点击'))

        self.btn_five.setShortcut('Alt+g')  # 快捷键是 alt+g

    def 实验空格快捷键(self):
        '''
        创建多个按钮
        初始化时，焦点在 btn_one 按钮上，按下空格，btn_one 文本 +1
        按 上下键 或 tab键 修改焦点，按下空格，查看是否是有焦点的按钮的文本 +1
        '''
        self.btn_one = QPushButton(self)
        self.btn_one.move(10, 10)
        self.btn_one.setText('1')
        self.btn_one.clicked.connect(lambda: self.btn_one.setText(str(int(self.btn_one.text()) + 1)))

        self.btn_two = QPushButton(self)
        self.btn_two.move(10, 60)
        self.btn_two.setText('1')
        self.btn_two.clicked.connect(lambda: self.btn_two.setText(str(int(self.btn_two.text()) + 1)))

        self.btn_three = QPushButton(self)
        self.btn_three.move(10, 110)
        self.btn_three.setText('1')
        self.btn_three.clicked.connect(lambda: self.btn_three.setText(str(int(self.btn_three.text()) + 1)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
