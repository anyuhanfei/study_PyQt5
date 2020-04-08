'''
221-QComboBox-简介

是一个组合控件
默认展示最小的空间给用户操作
可通过下拉选择界面, 选取更多的预置选项

构造出一个空白的下拉列表控件
后续通过操作数据的方法设置数据列表

继承自 QWidget

构造函数:
    QComboBox(parent: QWidget = None)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QComboBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('221-QComboBox-简介')
        self.resize(1000, 500)

        QComboBox(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
