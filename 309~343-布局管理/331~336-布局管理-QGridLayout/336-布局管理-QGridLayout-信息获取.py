'''
336-布局管理-QGridLayout-信息获取

cellRect(int row, int column)->QRect -- 某个块占的大小
columnCount()->int -- 列数
rowCount()->int -- 行数

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

        '''行数'''
        print(gl.rowCount())

        '''列数'''
        print(gl.columnCount())

        '''大小'''
        print(gl.cellRect(1, 1))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
