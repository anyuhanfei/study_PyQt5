'''
107-QButtonGroup-ID的操作.py

设置按钮对应的id

API：
    setId(QAbstractButton，int) -- 设置指定按钮的id
    id(QAbstractButton) -- 获取指定按钮的id, 不存在则返回-1
    checkedId() -- 获取被选中按钮的id, 不存在则返回 -1
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QButtonGroup


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('107_QButtonGroup_ID的操作.py')
        self.resize(1000, 500)

        '''初始化一组单选按钮'''
        rb_man = QRadioButton('男', self)
        rb_woman = QRadioButton('女', self)
        rb_man.move(10, 10)
        rb_woman.move(70, 10)
        sex_group = QButtonGroup(self)
        sex_group.addButton(rb_man)
        sex_group.addButton(rb_woman)

        '''设置指定按钮的id'''
        sex_group.setId(rb_man, 3)

        '''获取指定按钮的id'''
        print(sex_group.id(rb_man))

        '''获取被选中的按钮的id'''
        print(sex_group.checkedId())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
