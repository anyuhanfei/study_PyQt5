'''
109-QButtonGroup-信号

API:
    buttonClicked(int/QAbstractButton) -- 当按钮组中的按钮被点击时, 发射此信号
    buttonPressed(int/QAbstractButton) -- 当按钮组中的按钮被按下时, 发射此信号
    buttonReleased(int/QAbstractButton) -- 当按钮组中的按钮被释放时, 发射此信号
    buttonToggled(QAbstractButton/int, bool) -- 当按钮组中的按钮被切换状态时, 发射此信号

注：
    这些信号可以传按钮控件对象，也可以传按钮对应的id，但默认情况下传按钮控件对象，如果想要传按钮对应的id，那么可以在信号后面添加一个 '[int]' 字符串，如：group_obj.buttonClicked[int],connect(lambda)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QButtonGroup, QRadioButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('109_QButtonGroup_信号')
        self.resize(1000, 500)

        '''初始化一组单选按钮'''
        rb_man = QRadioButton('男', self)
        rb_woman = QRadioButton('女', self)
        rb_man.move(10, 10)
        rb_woman.move(70, 10)
        sex_group = QButtonGroup(self)
        sex_group.addButton(rb_man)
        sex_group.addButton(rb_woman)

        '''设置信号'''
        sex_group.buttonPressed.connect(lambda val: print(val))
        sex_group.buttonReleased[int].connect(lambda val: print(val))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
