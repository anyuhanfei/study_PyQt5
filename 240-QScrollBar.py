'''
240-QScrollBar

使用户能够访问比用于显示它的窗口小部件更大的文档部分
一般是结合QAbstractScrollArea使用
滚动条通常包括四个单独的控件：滑块，滚动箭头和页面控件

继承自 QAbstractSlider

功能作用继承自父类, 注意, 控件尺寸需要手动调整

信号同样继承自父类
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QScrollBar


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('240-QScrollBar')
        self.resize(1000, 500)

        QScrollBar(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
