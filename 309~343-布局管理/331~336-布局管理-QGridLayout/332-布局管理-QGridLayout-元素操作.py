'''
331-布局管理-QGridLayout-简介

控件:
    addWidget(self, QWidget)
    addWidget(self, QWidget, int row, int col, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
    addWidget(self, QWidget, int fromRow, int fromCol, int rowSpan, int colSpan, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())

布局:
    addLayout(self, QLayout, int row, int col, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())
    addLayout(self, QLayout, int FromRow, int fromCol, int rowSpan, int colSpan, alignment: Union[Qt.Alignment, Qt.AlignmentFlag] = Qt.Alignment())

获取:
    getItemPosition(self, int)->Tuple(int, int, int, int) -- 位置获取
    itemAtPosition(int row, int column) -- 条目获取

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QGridLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('331-布局管理-QGridLayout-简介')
        self.resize(1000, 600)

        gl = QGridLayout()

        label_1 = QLabel()
        label_1.setStyleSheet('background-color: red;')
        label_2 = QLabel()
        label_2.setStyleSheet('background-color: yellow;')
        label_3 = QLabel()
        label_3.setStyleSheet('background-color: blue;')

        '''指定位置'''
        gl.addWidget(label_1, 0, 0)
        gl.addWidget(label_2, 0, 2)

        '''指定位置和跨越多少行多少列'''
        gl.addWidget(label_3, 1, 1, 2, 2)

        self.setLayout(gl)

        '''获取位置'''
        print(gl.getItemPosition(1))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
