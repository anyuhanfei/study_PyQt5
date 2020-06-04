'''
340-布局管理-QStackedLayout-展示模式

setStackingMode(self, QStackedLayout.StackingMode)
stackingMode(self)->QStackedLayout.StackingMode

附:
    QStackedLayout.StackOne -- 只有当前小控件可见(默认)
    QStackedLayout.StackAll -- 所有小部件可见

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QStackedLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('340-布局管理-QStackedLayout-展示模式')
        self.resize(1000, 500)

        sl = QStackedLayout()
        self.setLayout(sl)

        label_1 = QLabel('aaa')
        label_2 = QLabel('bbb')
        label_1.setFixedSize(100, 100)
        label_1.setStyleSheet('background-color: red;')
        label_2.setStyleSheet('background-color: blue;')

        sl.addWidget(label_1)
        sl.addWidget(label_2)

        '''修改展示模式'''
        sl.setStackingMode(QStackedLayout.StackAll)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
