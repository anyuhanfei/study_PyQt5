'''
319-布局管理-基类-QBoxLayout-伸缩因子修改

设置伸缩因子:
    setStretchFactor(self, QWidget, int)-> bool
    setStretchFactor(self, QLayout, int)-> bool

设置布局管理器中的某个控件的伸缩因子, 若这个控件不在布局管理器中,则返回False

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
        self.layout.addWidget(label2)
        self.layout.addWidget(label3)

        '''设置子控件或子布局管理器的伸缩因子'''
        self.layout.setStretchFactor(label1, 1)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
