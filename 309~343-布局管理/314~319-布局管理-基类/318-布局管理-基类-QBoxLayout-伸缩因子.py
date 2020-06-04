'''
318-布局管理-基类-QBoxLayout-伸缩因子

添加伸缩:
    addStretch(self, stretch: int = 0)
    insertStretch(self, int, stretch: int = 0)
    stretch(int index)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QBoxLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('317-布局管理-基类-QBoxLayout-添加空白')
        self.resize(1000, 500)

        label1 = QLabel('标签1')
        label2 = QLabel('标签2')
        label3 = QLabel('标签3')
        label1.setStyleSheet('background-color: cyan;')
        label2.setStyleSheet('background-color: red;')
        label3.setStyleSheet('background-color: yellow;')

        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.layout.addWidget(label1)
        self.layout.addWidget(label2, 1)  # 参数二是设置伸缩因子
        self.layout.addWidget(label3, 1)

        '''添加空白的伸缩因子'''
        self.layout.addStretch(2)

        '''插入空白的伸缩因子'''
        self.layout.insertStretch(1, 1)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
