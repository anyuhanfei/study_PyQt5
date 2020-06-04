'''
337-布局管理-QStackedLayout

提供一个堆叠起来的布局, 在同一时刻只能显示一个控件
里面提供了相关方法, 可以切换控件

注意: 布局对象创建完成后, 需要立即绑定父控件或父布局

QStackedLayout()
QStackedLayout(QWidget)
QStackedLayout(QLayout)

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QStackedLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('337-布局管理-QStackedLayout')
        self.resize(1000, 500)

        sl = QStackedLayout()
        self.setLayout(sl)

        label_1 = QLabel()
        label_2 = QLabel()
        label_1.setStyleSheet('background-color: red;')
        label_2.setStyleSheet('background-color: blue;')

        sl.addWidget(label_1)
        sl.addWidget(label_2)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
