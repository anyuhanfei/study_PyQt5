'''
279-QLabel-对齐间距和缩进

API:
    对齐:
        alignment() -> Qt.Alignment -- 获取对齐
        setAlignment(Qt.Alignment) -- 设置对齐
    缩进和边距:
        setIndent(int) -- 设置缩进(仅限制对齐的一面)
        indent() -> int -- 获取缩进
        setMargin(int) -- 设置边距(限制四面)
        margin() -> int -- 获取边距
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('279-QLabel-对齐间距和缩进')
        self.resize(1000, 500)

        label = QLabel('测试', self)
        label.resize(300, 300)
        label.move(10, 10)
        label.setStyleSheet('background-color: yellow;')

        '''对齐'''
        label.setAlignment(Qt.AlignRight)  # 水平靠右

        '''边距'''
        label.setMargin(10)

        '''缩进'''
        label.setIndent(100)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
