'''
338-布局管理-QStackedLayout-添加插入获取控件

addWidget(self, QWidget)->int -- 添加控件
insertWidget(self, int QWidget)->int -- 插入控件
widget(self, int index)->QWidget
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QStackedLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('338-布局管理-QStackedLayout-添加插入获取控件')
        self.resize(1000, 500)

        sl = QStackedLayout()
        self.setLayout(sl)

        label_1 = QLabel()
        label_2 = QLabel()
        label_1.setStyleSheet('background-color: red;')
        label_2.setStyleSheet('background-color: blue;')

        '''添加控件'''
        sl.addWidget(label_1)

        '''插入控件'''
        sl.insertWidget(0, label_2)

        '''获取索引位置的控件'''
        sl.widget(1).setText('xxx')

        '''
        默认展示索引值为0的控件,在插入控件时,
        即使插入的位置是0, 并且成功插入, 那么其后索引的控件都会退一步, 同时展示的索引值也会退一步, 所以展示的控件不变
        '''


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
