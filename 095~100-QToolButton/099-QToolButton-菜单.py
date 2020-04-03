'''
099-QToolButton-菜单

工具按钮可以向普通按钮有下拉菜单，菜单中的行为功能、子菜单的行为功能都属于菜单，而不是工具按钮。

API：
    setMenu(QMenu) -- 设置菜单
    menu() -- 获取菜单对象

工具按钮唤起下拉菜单有多种方式，可以长按、单机、点击箭头等方式。

API：
    setPopupMode(QToolButton.ToolButtonPopupMode) -- 设置菜单唤起方式
    popupMode() -- 获取菜单唤起方式

QToolButton.DelayedPopup -- 鼠标按住一会才显示，类似于浏览器后退按钮
QToolButton.MenuButtonPopup -- 有一个专门的指示箭头，点击箭头才显示
QToolButton.InstantPopup -- 点了按钮就显示，点击信号不会发射
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QToolButton, QMenu, QAction


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('099_QToolButton_菜单')
        self.resize(1000, 500)

        '''设置一个简单的菜单'''
        self.menu = QMenu()
        self.action = QAction('行为动作')
        self.action.triggered.connect(lambda: print('点击了'))
        self.menu.addAction(self.action)

        toolb = QToolButton(self)
        toolb.setText('...')

        '''添加一个菜单'''
        toolb.setMenu(self.menu)

        '''设置唤起方式'''
        toolb.setPopupMode(QToolButton.MenuButtonPopup)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
