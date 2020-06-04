'''
311-布局管理-步骤总结

创建一个窗口控件, 然后再创建一个布局管理器, 将布局管理器设置到窗口控件中, 这样布局管理器就接管了这个窗口控件的布局管理功能.

然后若要在窗口控件内添加子控件, 那么可以将子控件添加到布局管理器中, 这样布局管理器自动将子控件加入到窗口控件中, 并且自动布局, 并且自动添加父子关系.
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('311-布局管理-步骤总结')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
