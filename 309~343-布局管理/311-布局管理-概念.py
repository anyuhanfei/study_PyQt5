'''
311-布局管理-概念

Qt包含一个布局管理类的集合, 它们被用来描述控件如何在应用程序的用户界面中呈现的
当可用空间发生变化时, 这些布局将自动调整控件的位置和大小
布局管理器不是界面控件, 而是界面控件的"定位策略"

所有QWidget类别及其子类都可以用布局来管理它们的子控件:
    布置子控件
    最高层窗口可感知的默认大小
    最高层可感知的最小大小
    调整大小的处理
    当内容改变的时候自动更新:
        字体大小, 文本或子控件的其他内容
        隐藏或显示子控件
        移除一些子控件

布局管理器的继承图:

QLayout -> QBoxLayout -> QHBoxLayout
                      -> QVBoxLayout
        -> QGridLayout
        -> QStackedLayout
        -> QFormLayout

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('311-布局管理-概念')
        self.resize(1000, 600)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
