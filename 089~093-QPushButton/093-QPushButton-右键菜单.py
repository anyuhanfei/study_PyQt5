'''
093-QPushButton-右键菜单

右键菜单的功能也属于信号的一种，QPushButton 的信息继承于 QWidget 和 QAbstractButton 类。其中可以实现右键菜单功能的信号是继承于 QWidget。

默认情况下，QWidget 控件及其子控件右键点击会触发 contextMenuEvent() 方法

如果要设置自定义右键点击，可以使用 setContextMenuPolicy(Qt.CustomContextMenu) 方法，其中参数代表的意思就是自定义右键，如果需要修改为默认右键点击，可以将参数修改为 Qt.DefaultContextMenu。

如果设置了自定义右键，那么右键所发射的信号将是 customContextMenuRequested(QPoint)。

注：自定义右键一般用于非面向对象编程，默认右键一般用于面向对象编程
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMenu, QAction


class Window(QWidget):
    widget = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('093_QPushButton_右键菜单')
        self.resize(1000, 500)

    def contextMenuEvent(self, event):
        '''右键点击控件即执行'''

        # 创建一个菜单
        self.menu = QMenu()
        self.action = QAction('行为动作')
        self.action.triggered.connect(lambda: print('点击了'))
        self.menu.addAction(self.action)

        # 菜单展示
        self.menu.exec_(event.globalPos())  # 全局坐标


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    '''自定义右键'''
    # from PyQt5.Qt import Qt
    # window.setContextMenuPolicy(Qt.CustomContextMenu)
    # window.customContextMenuRequested.connect(lambda point: print('点击坐标位置：%s' % (point)))

    window.show()

    sys.exit(app.exec_())
