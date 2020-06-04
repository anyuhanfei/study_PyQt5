'''
339-布局管理-QStackedLayout-切换

setCurrentIndex(self, int) -- 通过索引值切换
currentIndex(self)->int -- 获取当前展示索引值
setCurrentWidget(self, QWidget) -- 通过控件切换
currentWidget(self)->QWidget -- 获取当前展示控件

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QStackedLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('339-布局管理-QStackedLayout-切换')
        self.resize(1000, 500)

        sl = QStackedLayout()
        self.setLayout(sl)

        label_1 = QLabel()
        label_2 = QLabel()
        label_1.setStyleSheet('background-color: red;')
        label_2.setStyleSheet('background-color: blue;')

        sl.addWidget(label_1)
        sl.addWidget(label_2)

        '''切换'''
        sl.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
