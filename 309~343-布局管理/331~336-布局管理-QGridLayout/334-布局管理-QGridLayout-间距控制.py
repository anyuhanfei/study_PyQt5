'''
334-布局管理-QGridLayout-间距控制

setVerticalSpacing(int spacing) -- 设置垂直方向的间距
verticalSpacing()->int -- 获取
setHorizontalSpacing(int spacing) -- 设置水平方向的间距
horizontalSpacing()->int -- 获取
setSpacing(int spacing) -- 设置两个方向的间距
spacing()->int -- 获取

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('334-布局管理-QGridLayout-间距控制')
        self.resize(1000, 600)

        gl = QGridLayout()

        label_1 = QLabel()
        label_1.setStyleSheet('background-color: red;')
        label_2 = QLabel()
        label_2.setStyleSheet('background-color: yellow;')
        label_3 = QLabel()
        label_3.setStyleSheet('background-color: blue;')

        gl.addWidget(label_1, 0, 0)
        gl.addWidget(label_2, 0, 1)
        gl.addWidget(label_3, 1, 0, 1, 2)

        self.setLayout(gl)

        '''设置水平间距'''
        gl.setHorizontalSpacing(30)

        '''设置垂直间距'''
        gl.setVerticalSpacing(50)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
