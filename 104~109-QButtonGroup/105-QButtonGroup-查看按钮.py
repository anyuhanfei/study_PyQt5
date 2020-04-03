'''
105-QButtonGroup-查看按钮

API
    buttons() -- 查看所有按钮组中的按钮
    button(ID) -- 根据ID获取对应按钮, 没有则返回None
    checkedButton() -- 获取选中的那个按钮
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QButtonGroup, QRadioButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('105_QButtonGroup_查看按钮')
        self.resize(1000, 500)

        '''初始化一组单选按钮'''
        rb_man = QRadioButton('男', self)
        rb_woman = QRadioButton('女', self)
        rb_man.move(10, 10)
        rb_woman.move(70, 10)
        sex_group = QButtonGroup(self)
        sex_group.addButton(rb_man)
        sex_group.addButton(rb_woman)

        '''查看组中的所有按钮'''
        print(sex_group.buttons())

        '''查看组中某个id的按钮'''
        print(sex_group.button(-2))

        '''查看组中选中的按钮'''
        rb_woman.setChecked(True)
        print(sex_group.checkedButton())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
