'''
106_QButtonGroup_移除按钮

将按钮组中的其中一个按钮移出组，并不是删除按钮

API：
    removeButton(QAbstractButton) -- 移除指定按钮
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QButtonGroup


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('106_QButtonGroup_移除按钮')
        self.resize(1000, 500)

        '''初始化一组单选按钮'''
        rb_man = QRadioButton('男', self)
        rb_woman = QRadioButton('女', self)
        rb_man.move(10, 10)
        rb_woman.move(70, 10)
        sex_group = QButtonGroup(self)
        sex_group.addButton(rb_man)
        sex_group.addButton(rb_woman)

        '''将其中一个按钮移除按钮组'''
        # 若下面的代码生效，那么两个按钮将不会互斥
        sex_group.removeButton(rb_man)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
