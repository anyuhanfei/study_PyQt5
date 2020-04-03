'''
104-QButtonGroup-创建

提供 一个抽象的按钮容器, 可以将多个按钮划分为一组
不具备可视化的效果
一般放的都是可以被检查的按钮(单选按钮和复选按钮)

API:
    QButtonGroup(parent) -- 创建按钮组
    addButton(QAbstractButton, id = -1) -- 添加一个按钮，不传入id参数的话，自动分配的id为负数，所以传入的id参数一般为正数

注：
    自动分配的id从 -2 开始
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QButtonGroup


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('104_QButtonGroup_创建')
        self.resize(1000, 500)

        '''初始化两组单选按钮'''
        rb_man = QRadioButton('男', self)
        rb_woman = QRadioButton('女', self)
        rb_man.move(10, 10)
        rb_woman.move(70, 10)

        rb_yes = QRadioButton('yes', self)
        rb_no = QRadioButton('no', self)
        rb_yes.move(10, 50)
        rb_no.move(70, 50)

        '''创建按钮组'''
        sex_group = QButtonGroup(self)
        judge_group = QButtonGroup(self)

        '''向按钮组中添加按钮'''
        sex_group.addButton(rb_man)
        sex_group.addButton(rb_woman)
        judge_group.addButton(rb_yes)
        judge_group.addButton(rb_no)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
