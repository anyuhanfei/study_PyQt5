'''
085_QAbstractButton_排他性

如果同时存在多个按钮, 而此时所有按钮又设置了排他性, 则在同一时刻只能选中一个按钮

最典型的就是单选框，只能选择其中的一个选项。

API:
    autoExclusive() -- 是否自动排他
    setAutoExclusive(bool) -- 设置自动排他

在同级别下(有相同父控件)，具有排他性的按钮才能相互排他
    没有排他性的按钮被选中，再次选中具有排他性的按钮后，没有排他性的按钮不会改变被选中的状态.
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
        btn_one.setCheckable(True)  # 设置为可被选中状态

        btn_two = QPushButton(self)
        btn_two.setText('btn_two')
        btn_two.move(10, 40)
        btn_two.setCheckable(True)

        btn_three = QPushButton(self)
        btn_three.setText('btn_three')
        btn_three.move(10, 70)
        btn_three.setCheckable(True)

        '''设置按钮控件的排他性'''
        btn_two.setAutoExclusive(True)
        btn_three.setAutoExclusive(True)

        '''获取按钮控件的排他性'''
        btn_one_is_auto_exclusive = btn_one.autoExclusive()
        btn_two_is_auto_exclusive = btn_two.autoExclusive()
        btn_three_is_auto_exclusive = btn_three.autoExclusive()

        # 打印
        label = QLabel(self)
        label.setText('btn_one 的排他性：%s' % (btn_one_is_auto_exclusive))
        label.move(10, 100)

        label = QLabel(self)
        label.setText('btn_two 的排他性：%s' % (btn_two_is_auto_exclusive))
        label.move(10, 130)

        label = QLabel(self)
        label.setText('btn_three 的排他性：%s' % (btn_three_is_auto_exclusive))
        label.move(10, 160)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
