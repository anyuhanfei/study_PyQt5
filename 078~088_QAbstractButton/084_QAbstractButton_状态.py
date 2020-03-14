'''
084_QAbstractButton_状态

按钮可以向外界展示自己几种不同的状态，供用户做一个参考判定。例如：用户登录时，如果不输入账号和密码，登录按钮就是无法点击的状态。

无法点击状态是继承于 QWidget ，除去无法点击的状态，还有按下按钮状态和选中按钮状态。

API:
    isDown() -- 是否按下按钮
    setDown(bool) -- 设置按钮, 是否被按下
    isChecked() -- 按钮是否可以被选中
    setCheckable(bool) -- 设置按钮, 是否可以被选中
    setChecked(bool) -- 设置按钮, 是否被选中
    toggle() -- 切换选中与非选中状态
    isEnabled() -- 按钮是否可以使用
    setEnabled(bool) -- 设置按钮是否可以使用
'''

import sys


from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('084_QAbstractButton_状态')
        self.resize(500, 500)

        btn_one = QPushButton(self)
        btn_one.setText('btn_one')
        btn_one.move(10, 10)

        btn_two = QPushButton(self)
        btn_two.setText('btn_two')
        btn_two.move(10, 40)

        btn_three = QPushButton(self)
        btn_three.setText('btn_three')
        btn_three.move(10, 70)

        btn_four = QPushButton(self)
        btn_four.setText('btn_four')
        btn_four.move(10, 100)

        btn_five = QPushButton(self)
        btn_five.setText('btn_five')
        btn_five.move(10, 130)

        '''按下状态'''
        # 设置按钮是按下状态
        btn_one.setDown(True)  # True 按下  False 非按下

        # 获取按钮是否是按下状态
        btn_one_is_down = btn_one.isDown()

        '''选中状态'''
        # 设置为可被选中状态，默认情况下，按钮是不可被选中状态，单选框和多选框是可被选中状态
        # 大概情形为：点击按钮后，按钮被选中，会呈现与鼠标点击不放时相同的样子
        btn_two.setCheckable(True)  # True 可被选中  False 不可被选中

        # 获取按钮是否为可被选中状态
        btn_two_is_checkable = btn_two.isCheckable()

        # 设置为选中状态
        btn_three.setCheckable(True)  # 不可被选中的按钮必须设置为可被选中后才能将控件设置为选中
        btn_three.setChecked(True)  # True 选中  False 非选中

        # 切换按钮的选中状态
        btn_four.setCheckable(True)
        btn_four.toggle()  # 当按钮是非选中状态，那么执行此方法后按钮就变成选中状态，反之亦然

        # 获取按钮是否为选中状态
        btn_three_is_checked = btn_three.isChecked()
        btn_four_is_checked = btn_four.isChecked()

        '''可用状态'''
        # 设置按钮的可用状态
        btn_five.setEnabled(False)  # 默认情况下，按钮时可用状态

        # 获取按钮的可用状态
        btn_five_is_enabled = btn_five.isEnabled()

        '''补充：修改按钮被按下的样式'''
        btn_one.setStyleSheet("QPushButton:pressed {background-color: red;}")

        label = QLabel(self)
        label.setText('btn_one 是否被按下：%s' % (btn_one_is_down))
        label.move(10, 200)

        label = QLabel(self)
        label.setText('btn_two 是否是可选中：%s' % (btn_two_is_checkable))
        label.move(10, 230)

        label = QLabel(self)
        label.setText('btn_three 是否被选中：%s' % (btn_three_is_checked))
        label.move(10, 260)

        label = QLabel(self)
        label.setText('btn_four 是否被选中：%s' % (btn_four_is_checked))
        label.move(10, 290)

        label = QLabel(self)
        label.setText('btn_five 是否可用：%s' % (btn_five_is_enabled))
        label.move(10, 320)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
