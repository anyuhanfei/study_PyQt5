'''
333-布局管理-QGridLayout-最小列宽行高和拉伸系数

setColumnMinimumWidth(int column, int minSize) -- 设置某列最小宽度
columnMinimumWidth(int column)->int -- 获取
setRowMinimumHeight(int row, int minSize) -- 设置某行最小行高
rowMinimumHeight(int row)->int -- 获取
setColumnStretch(int column, int stretch) -- 设置某列的拉伸系数
columnStretch(int column)->int -- 获取
setRowStretch(int row, int stretch) -- 设置某行的拉伸系数
rowStretch(int row)->int -- 获取

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('333-布局管理-QGridLayout-最小列宽行高和拉伸系数')
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

        '''设置列最小宽度'''
        gl.setColumnMinimumWidth(0, 100)

        '''设置行最小高度'''
        gl.setRowMinimumHeight(0, 100)

        '''设置列拉伸系数'''
        gl.setColumnStretch(0, 1)
        gl.setColumnStretch(1, 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
