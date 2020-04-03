'''
100-QToolButton-信号

除去继承父类的信号外，QToolButton 还有一个信号：
    triggered(QAction *action) -- 当点击工具按钮下菜单的某个action时触发, 并会将action传递出来

小技巧：
    可以在 action 中通过 setData() 方法设置唯一标识，当触发 action 时，在 triggered 信号对应的槽函数中验证这个唯一标识，即可在一个方法内写多个 action 的业务逻辑。

注意：
    action 自身的 triggered 信号会与 action 的 triggered 同时触发
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QToolButton, QMenu, QAction


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('098_QToolButton_自动提升')
        self.resize(1000, 500)

        '''设置一个简单的菜单, 设置 triggered 信号连接的槽函数，设置一个标识'''
        self.menu = QMenu()
        self.action1 = QAction('行为动作1')
        self.action2 = QAction('行为动作2')
        self.action1.triggered.connect(lambda: print('点击了行为动作1'))
        self.action2.triggered.connect(lambda: print('点击了行为动作2'))
        self.action1.setData('1')
        self.action2.setData('2')
        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)

        toolb = QToolButton(self)
        toolb.setText('...')

        '''添加一个菜单'''
        toolb.setMenu(self.menu)

        '''设置唤起方式'''
        toolb.setPopupMode(QToolButton.MenuButtonPopup)

        '''设置 triggered 信号'''
        # 通过合理使用 action 中的标识来实现业务逻辑
        toolb.triggered.connect(lambda action: print('点击了行为动作%s' % (action.data())))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
