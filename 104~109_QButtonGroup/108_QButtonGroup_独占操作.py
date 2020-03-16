'''
108_QButtonGroup_独占操作

API：
    setExclusive(bool) -- 设置组内的按钮是否独占
    exclusive() -- 查看组内的按钮是否独占
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QButtonGroup, QRadioButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('108_QButtonGroup_独占操作')
        self.resize(1000, 500)

        '''初始化一组单选按钮'''
        rb_man = QRadioButton('男', self)
        rb_woman = QRadioButton('女', self)
        rb_man.move(10, 10)
        rb_woman.move(70, 10)
        sex_group = QButtonGroup(self)
        sex_group.addButton(rb_man)
        sex_group.addButton(rb_woman)

        '''将按钮组设置为不独占'''
        sex_group.setExclusive(False)

        '''查看按钮组是否为独占'''
        print(sex_group.exclusive())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
