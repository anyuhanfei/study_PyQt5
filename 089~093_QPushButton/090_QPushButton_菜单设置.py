'''
090_QPushButton_菜单设置

当点击按钮后，可以展示一系列的下拉菜单

API
    setMenu(QMenu) -- 设置菜单
    menu() -- 获取菜单
    showMenu() -- 展示菜单

相关知识：
    QMenu 菜单控件，父类为 QtWidgets，可以作为子菜单的容器。
    QAction 行为动作菜单控件，父类为 QtWidgets，被点击时会发出 triggered 信号，可以通过连接槽函数进行一些操作

注意：
    如果使用面向对象编程，菜单控件必须是类中的属性，而不是临时变量
    有子菜单或子行为动作的子菜单展示在父菜单中只能用 addMenu() 方法，不要绑定父类 (重要)
        经过测试，初次子菜单设置了父菜单(setParent() 方法)，也拥有自己的子菜单和行为动作，就算使用 addMenu() 方法，也只是在父菜单中展示了子菜单自身，无法展示出自己的子菜单。
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QMenu, QAction


class Window(QWidget):
    widget = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('090_QPushButton_菜单设置')
        self.resize(1000, 500)

        self.btn = QPushButton(self)
        self.btn.setText('xxx')
        self.btn.move(10, 10)

        '''创建一个菜单控件'''
        self.menu = QMenu()

        '''添加子菜单'''
        '''行为动作'''
        # 行为动作菜单创建
        self.action_one = QAction('行为动作')
        # 行为动作信号
        self.action_one.triggered.connect(self._triggered)

        self.action_two = QAction('行为动作')
        self.action_two.triggered.connect(self._triggered)

        '''子菜单'''
        # 创建一个菜单控件
        self.child_menu = QMenu()
        # 设置菜单控件提示文本
        self.child_menu.setTitle('子菜单')
        # 添加行为动作菜单到这个子菜单中
        self.child_menu.addAction(self.action_two)

        '''将子菜单添加到菜单控件中'''
        # 行为
        self.menu.addAction(self.action_one)
        # 分割线
        self.menu.addSeparator()
        # 子菜单
        self.menu.addMenu(self.child_menu)

        '''将菜单控件添加至按钮控件中'''
        self.btn.setMenu(self.menu)

        '''获取菜单'''
        menu_obj = self.btn.menu()

        label = QLabel(self)
        label.setText(str(menu_obj))
        label.move(150, 10)

    def _triggered(self):
        self.widget += 30
        label = QLabel(self)
        label.setText('点击 行为动作')
        label.move(10, self.widget)
        label.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    '''展示菜单(必须写在窗口展示之后)'''
    window.btn.showMenu()

    sys.exit(app.exec_())
