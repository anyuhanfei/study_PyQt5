'''
102-QRadioButton-信号

QRadioButton 继承了 QAbstractButton 的所有信号，其中最常用的就是 toggled 切换信号。

当单选按钮控件状态改变时，也就是改变选中状态时，都会发出 toggled 信号。并且会给一个是否是选中状态的参数
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('102_QRadioButton_信号')
        self.resize(1000, 500)

        '''初始化一些单选按钮'''
        rb_one = QRadioButton('rb_one', self)
        rb_two = QRadioButton('rb_two', self)
        rb_one.move(10, 10)
        rb_two.move(100, 10)

        '''toggled 信号'''
        rb_one.toggled.connect(lambda is_check: print('rb_one 是否是选中状态：%s' % (is_check)))
        rb_two.toggled.connect(lambda is_check: print('rb_two 是否是选中状态：%s' % (is_check)))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
