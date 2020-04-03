'''
080-QAbstractButton-文本设置

QAbstractButton 文本设置功能有以下两个 API，这些在前文学习中已经附带着学过了：
    setText() -- 设置按钮提示文本
    text() -- 获取按钮提示文本

案例：
    创建一个按钮，初始文本为 1，每点击一次，则让数字增加 1
'''

import sys


from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('080_QAbstractButton_文本设置')
        self.resize(500, 500)

        self.btn = QPushButton(self)
        self.btn.setText('1')  # 必须是字符串类型
        # 设置点击信息的槽函数
        self.btn.clicked.connect(lambda: self.btn.setText(str(int(self.btn.text()) + 1)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
