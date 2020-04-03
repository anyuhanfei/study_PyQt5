'''
101-QRadioButton-基础

一般给用户提供若干选项的单选操作，当选中其中一个时，其他选中会自动取消。
此按钮左侧会有一个圆圈图标, 用于标识用户的选中状态

QRadioButton 继承自 QAbstractButton 类，QAbstractButton 类中的所有方法 QRadiobutton 均适用。

单选按钮控件的特性是因为有一个独占(setAutoExclusive)的特性，如果手动关闭，那么单选按钮控件的最基本的功能将失效。
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('101_QRadioButton_基础')
        self.resize(1000, 500)

        '''创建'''
        # 方法一
        rb_one = QRadioButton(self)
        rb_one.setText('rb_one')
        rb_one.move(10, 10)

        # 方法二
        rb_two = QRadioButton('rb_two', self)
        rb_two.move(100, 10)

        '''设置图标'''
        icon = QIcon('./xxx.png')
        rb_two.setIcon(icon)

        '''设置默认点击'''
        rb_two.setChecked(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
